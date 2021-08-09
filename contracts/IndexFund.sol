// SPDX-License-Identifier: MIT
pragma solidity >=0.8.4;

import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "./interfaces/IERC20Burnable.sol";

contract IndexFund {
    using SafeERC20 for IERC20Burnable;

    address private constant PILOT_ADDRESS = 0x50cdc3cFdF3ee67c43C12d8e6c9dccA29a4FC9bc; //dummy

    address private TIMELOCK;

    uint256 private constant PRECISION = 10**18;

    address[] lockedFundAddresses;

    mapping(bytes32 => bool) private withdraws;

    modifier onlyTimelock() {
        require(msg.sender == TIMELOCK, "INDEX_FUND:: NOT_TIMELOCK");
        _;
    }

    constructor(address _timelock) public {
        TIMELOCK = _timelock;
    }

    function withdraw(
        address[] memory _tokenAddresses,
        uint256 _pilotAmount,
        bool _value
    ) external {
        uint256 pilotPercentage;

        uint256 tokenBalance;

        uint256 circulatingPilotSupply = circulatingSupply();

        uint256 timestamp = block.timestamp;

        address payable sender = payable(msg.sender);

        address contractAddress = address(this);

        pilotPercentage = (_pilotAmount * PRECISION) / circulatingPilotSupply;

        IERC20Burnable(PILOT_ADDRESS).burnFrom(sender, _pilotAmount);

        for (uint256 i = 0; i < _tokenAddresses.length; i++) {
            bytes32 withdrawnId = keccak256(abi.encode(_tokenAddresses[i], sender, timestamp));
            require(withdraws[withdrawnId] == false, "INDEXFUND:: TOKEN_ALREADY_WITHDRAWN");

            tokenBalance = IERC20(_tokenAddresses[i]).balanceOf(contractAddress);

            uint256 tokenPercentageToTransfer = (tokenBalance * pilotPercentage) / PRECISION;

            withdraws[withdrawnId] = true;

            IERC20Burnable(_tokenAddresses[i]).safeTransfer(sender, tokenPercentageToTransfer);
        }

        if (_value) {
            tokenBalance = contractAddress.balance;
            require(tokenBalance > 0, "INDEXFUND:: INSUFFICIENT_ETH");
            sender.transfer((tokenBalance * pilotPercentage) / PRECISION);
        }
    }

    function addLockedFundsAddresses(address[] memory _accounts) external onlyTimelock {
        for (uint24 i = 0; i < _accounts.length; i++) {
            require(_accounts[i] != address(0), "INDEX_FUND:: ZERO_ADDRESS");
            lockedFundAddresses.push(_accounts[i]);
        }
    }

    function removeLockedFundsAddress(uint256 _index) external onlyTimelock {
        require(lockedFundAddresses[_index] != address(0), "INDEX_FUND:: ELEMENT_NOT_EXISTS");
        delete lockedFundAddresses[_index];
    }

    function migrateFunds(address payable _newVersion, address[] calldata tokens) external onlyTimelock {
        address thisContract = address(this);

        for (uint24 i = 0; i < tokens.length; i++) {
            IERC20Burnable(tokens[i]).safeTransferFrom(
                thisContract,
                _newVersion,
                IERC20Burnable(tokens[i]).balanceOf(thisContract)
            );
        }
        if (thisContract.balance > 0) {
            _newVersion.transfer(thisContract.balance);
        }
    }

    function circulatingSupply() public view returns (uint256 circulatingSupply) {
        uint256 totalLocked;
        for (uint24 i = 0; i < lockedFundAddresses.length; i++) {
            totalLocked += IERC20Burnable(PILOT_ADDRESS).balanceOf(lockedFundAddresses[i]);
        }
        circulatingSupply = IERC20Burnable(PILOT_ADDRESS).totalSupply() - totalLocked;
    }

    fallback() external payable {}

    receive() external payable {}
}
