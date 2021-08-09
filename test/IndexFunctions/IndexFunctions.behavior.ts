import { SignerWithAddress } from "@nomiclabs/hardhat-ethers/dist/src/signer-with-address";
import { Contract } from "ethers";
import { shouldBehaveLikeWithdraw } from "../Withdraw/withdraw.behavior";
export async function shouldBehaveLikeIndexFunctions(
  wallets: SignerWithAddress[],
  indexFund: Contract,
  pilotToken: Contract,
  flashToken: Contract,
): Promise<void> {
  describe("TESTING GET TOKEN", async () => {
    await shouldBehaveLikeWithdraw(indexFund, flashToken, pilotToken, wallets[0]);
  });
}
