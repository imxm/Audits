import { use } from "chai";
import { utils, Contract } from "ethers";
import { solidity } from "ethereum-waffle";
import { deployStubPilot, deployStubFlash, deployStubIndexFund, deployStubUsdt } from "./stubs";
import { shouldBehaveLikeIndexFunctions } from "./IndexFunctions/IndexFunctions.behavior";
import hre from "hardhat";
use(solidity);
describe("Testing IndexFund Contract", async () => {
  let indexFund: Contract;
  let pilotToken: Contract;
  let flashToken: Contract;
  let usdtToken: Contract;

  const [wallet0, wallet1, wallet2, wallet3, wallet4] = await hre.ethers.getSigners();

  before("Initiating the tests", async () => {
    pilotToken = await deployStubPilot(wallet0);
    await pilotToken.updateMinter(wallet0.address);
    await pilotToken.mint(wallet0.address, utils.parseEther("10000"));
    await pilotToken.mint(wallet1.address, utils.parseEther("100"));
    flashToken = await deployStubFlash(wallet0);
    usdtToken = await deployStubUsdt(wallet0);
    indexFund = await deployStubIndexFund(wallet0);
  });

  describe("TESTING INDEX FUND FUNCTIONS", async () => {
    it("Testing Index Functions", async () => {
      console.log("INDEX FUND", indexFund.address);
      console.log("FLASH TOKEN", flashToken.address);
      console.log("USDT TOKEN", usdtToken.address);
      await shouldBehaveLikeIndexFunctions([wallet0, wallet1, wallet2, wallet3], indexFund, pilotToken, flashToken);
      console.log("PILOT", pilotToken.address);
    });
  });
});
