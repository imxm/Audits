import IndexFundArtifact from "../artifacts/contracts/IndexFund.sol/IndexFund.json";
import { deployContract } from "ethereum-waffle";
import ERC20Artifact from "../artifacts/contracts/test/ERC20.sol/ERC20.json";
import PilotTokenArtifact from "./PilotTokenArtifact/Pilot.json";
import { SignerWithAddress } from "@nomiclabs/hardhat-ethers/signers";
import { BigNumber, Contract } from "ethers";

export async function deployStubIndexFund(deployer: SignerWithAddress): Promise<Contract> {
  const IndexFund = await deployContract(deployer, IndexFundArtifact, [deployer.address]);
  return IndexFund;
}

export async function deployStubFlash(deployer: SignerWithAddress): Promise<Contract> {
  const flash = await deployContract(deployer, ERC20Artifact, ["Flash", "FLASH"]);
  return flash;
}

export async function deployStubPilot(deployer: SignerWithAddress): Promise<Contract> {
  const pilot = await deployContract(deployer, PilotTokenArtifact, [
    deployer.address,
    [deployer.address],
    [BigNumber.from("100")],
  ]);
  return pilot;
}

export async function deployStubUsdt(deployer: SignerWithAddress): Promise<Contract> {
  const usdt = await deployContract(deployer, ERC20Artifact, ["Usdt", "USDT"]);
  return usdt;
}
