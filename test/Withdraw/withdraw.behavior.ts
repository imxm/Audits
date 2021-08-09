import { Contract } from "@ethersproject/contracts";
import { BigNumber, utils } from "ethers";
import { expect } from "chai";
import { SignerWithAddress } from "@nomiclabs/hardhat-ethers/dist/src/signer-with-address";

const ZERO_ADDRESS: string = "0x0000000000000000000000000000000000000000";
let pilotSupply: BigNumber;
let contractFlashBalance: BigNumber;
let userFLashBalance: BigNumber;
let userPilotBalance: BigNumber;
let pilotPercentage: BigNumber;
let flashToTransfer: BigNumber;
export async function shouldBehaveLikeWithdraw(
  indexFund: Contract,
  flashToken: Contract,
  pilotToken: Contract,
  wallet0: SignerWithAddress,
): Promise<void> {
  it("Should fail with token already withdrawn", async function () {
    await pilotToken.approve(indexFund.address, utils.parseEther("900000000"));
    await flashToken.transfer(indexFund.address, utils.parseEther("20000000"));
    await expect(
      indexFund.withdraw([flashToken.address, flashToken.address], utils.parseEther("200"), false),
    ).to.be.revertedWith("INDEXFUND:: TOKEN_ALREADY_WITHDRAWN");
  });

  it("Should successfully transfer the tokens", async function () {
    console.log("USER PILOT BALANCE BEFORE", (await pilotToken.balanceOf(wallet0.address)).toString());

    await pilotToken.approve(indexFund.address, utils.parseEther("900000000"));

    await flashToken.transfer(indexFund.address, utils.parseEther("20000000"));
    console.log("USER FLASH BALANCE BEFORE", (await flashToken.balanceOf(wallet0.address)).toString());
    expect(await indexFund.withdraw([flashToken.address], utils.parseEther("200"), false));
    console.log("USER FLASH BALANCE AFTER", (await flashToken.balanceOf(wallet0.address)).toString());
    console.log("USER PILOT BALANCE BEFORE", (await pilotToken.balanceOf(wallet0.address)).toString());
  });

  //it("User flash balance should be correctly updated", async function () {
  //  expect(await flashToken.balanceOf(wallet0.address)).to.be.equal(
  //    BigNumber.from(userFLashBalance),
  //  );
  //});

  //it("User pilot balance should be correctly deducted", async function () {
  //  expect(await pilotToken.balanceOf(wallet0.address)).to.be.equal(
  //    BigNumber.from(userPilotBalance),
  //  );
  //});

  //it("Contract flash balance should be correcty deducted", async function () {
  //  expect(await flashToken.balanceOf(indexFund.address)).to.be.equal(
  //    contractFlashBalance,
  //  );
  //});

  //it("Pilot total supply should be correctly decreased after burn", async function () {
  //  expect(await pilotToken.totalSupply()).to.be.equal(pilotSupply);
  //});

  it("Should successfully transfer ethers", async function () {
    wallet0.sendTransaction({
      from: wallet0.address,
      to: indexFund.address,
      value: utils.parseEther("1000"),
    });
    await pilotToken.approve(indexFund.address, utils.parseEther("900000000"));
    expect(await indexFund.withdraw([flashToken.address], utils.parseEther("200"), true));
  });
}
