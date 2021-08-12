const { expect } = require("chai");
const { waffle, ethers } = require("hardhat");
const { deployContract } = waffle;
const provider = waffle.provider;
const web3 = require("web3");
const { defaultAbiCoder, hexlify, keccak256, toUtf8Bytes, solidityPack } = require("ethers/lib/utils");
const { Wallet } = require("ethers");
const { Console, count } = require("console");

let contractDao;
let contractPHNX;
const proposalID = ["0", "1", "2", "3", "4"];

const issueFunds = web3.utils.toWei("500");

describe("Pilot Testing", function () {
  let pilotToken;
  let flashToken;
  let usdtToken;

  const [wallet0, wallet1, wallet2, wallet3, wallet4] = provider.getWallets();
  before(async () => {
    const pilotFactory = await ethers.getContractFactory("Pilot");
    pilotToken = await pilotFactory.deploy(wallet0.address, [wallet1.address], [wallet2.address]);
    await pilotToken.deployed();

    const uniFactory = await ethers.getContractFactory("Uni");
    const uni = await uniFactory.deploy(wallet0.address, wallet0.address, web3.utils.toWei("10000"));
    await uni.deployed();

    const linkFactory = await ethers.getContractFactory("LinkToken");
    const link = await linkFactory.deploy();
    await link.deployed();

    // const usdcFactory = await ethers.getContractFactory("DERC20");
    // const usdc = await usdtFactory.deploy("curve pegged dollar", "USDC");
    // await usdc.deployed();

    const bal = await uni.balanceOf(wallet0.address);
    console.log("uni bal of wallet0: ", bal.toString());

    // const burn = await pilotToken.burn(web3.utils.toWei("10000"));
    // console.log(burn);

    const IndexFactory = await ethers.getContractFactory("IndexFund");
    const indexFund = await IndexFactory.deploy(wallet0.address, [pilotToken.address], pilotToken.address);
    await indexFund.deployed();

    await uni.transfer(indexFund.address, web3.utils.toWei("1000"));
    await link.transfer(indexFund.address, web3.utils.toWei("1000"));

    const balUni = await uni.balanceOf(indexFund.address);
    console.log("bal of uni: ", balUni.toString());

    // await pilotToken.updateMinter(wallet0.address);

    // await pilotToken.mint(indexFund.address, web3.utils.toWei("10000"));
    // console.log("balance of indexFund: ", (await pilotToken.balanceOf(indexFund.address)).toString())
    // await usdt.transfer(wallet1.address, web3.utils.toWei("1000"));
    // await usdt.connect(wallet2).approve(wallet2.address, web3.utils.toWei("1000"))
    // await usdt.connect(wallet2).transferFrom(wallet2.address, wallet3.address, web3.utils.toWei("10"))

    await indexFund.migrateFunds(wallet3.address, [uni.address, link.address]);

    console.log("balance of wallet3: ", (await uni.balanceOf(wallet3.address)).toString());

    // transfer usdt to index fund
    // await usdt._mint(indexFund.address, web3.utils.toWei("10000000"));
    // await usdc._mint(indexFund.address, web3.utils.toWei("10000000"));

    // const withDraw = await indexFund.withdraw([usdt.address], web3.utils.toWei("100"));
  });

  it("should do nothing", async () => {
    console.log("nothing");
  });
});
