# Mars Protocol

CosmWasm · 11 published reports · 149 findings

Mars money market across its generations: Red Bank, Fields of Mars, the Rover credit manager, Outposts, the Neutron deployment and Perps.

**Role:** Reviewer across the engagement.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| February 17, 2022 | [Mars](https://github.com/oak-security/audit-reports/blob/main/Mars/2022-02-17%20Audit%20Report%20-%20Mars%20v1.0.pdf) | 5 | 0 | 7 | 2 | 14 |
| February 17, 2022 | [Mars Periphery](https://github.com/oak-security/audit-reports/blob/main/Mars/2022-02-17%20Audit%20Report%20-%20Mars%20Periphery%20v1.0.pdf) | 0 | 1 | 5 | 2 | 8 |
| February 17, 2022 | [Fields of Mars](https://github.com/oak-security/audit-reports/blob/main/Mars/2022-02-17%20Audit%20Report%20-%20Fields%20of%20Mars%20v1.0.pdf) | 0 | 1 | 4 | 3 | 8 |
| December 9, 2022 | [Mars Rover](https://github.com/oak-security/audit-reports/blob/main/Mars/2022-12-09%20Audit%20Report%20-%20Mars%20Rover%20v1.0.pdf) | 1 | 1 | 6 | 8 | 16 |
| January 13, 2023 | [Mars Outposts](https://github.com/oak-security/audit-reports/blob/main/Mars/2023-01-13%20Audit%20Report%20-%20Mars%20Outposts%20v1.0.pdf) | 1 | 3 | 10 | 7 | 21 |
| February 3, 2023 | [Mars Periphery](https://github.com/oak-security/audit-reports/blob/main/Mars/2023-02-03%20Audit%20Report%20-%20Mars%20Periphery%20v1.0.pdf) | 1 | 2 | 3 | 7 | 13 |
| February 3, 2023 | [Mars Rover Updates](https://github.com/oak-security/audit-reports/blob/main/Mars/2023-02-03%20Audit%20Report%20-%20Mars%20Rover%20Updates%20v1.0.pdf) | 0 | 2 | 1 | 6 | 9 |
| August 1, 2023 | [Mars Red Bank Updates](https://github.com/oak-security/audit-reports/blob/main/Mars/2023-08-01%20Audit%20Report%20-%20Mars%20Red%20Bank%20Updates%20v1.0.pdf) | 3 | 4 | 5 | 2 | 14 |
|  | [Mars Rover v2](https://github.com/oak-security/audit-reports/blob/main/Mars/2023-09-14%20Audit%20Report%20-%20Mars%20Rover%20v2%20v1.0.pdf) | 1 | 5 | 6 | 9 | 21 |
| July 15, 2024 | [Mars v2 on Neutron](https://github.com/oak-security/audit-reports/blob/main/Mars/2024-07-15%20Audit%20Report%20-%20Mars%20v2%20on%20Neutron%20v1.0.pdf) | 2 | 4 | 1 | 8 | 15 |
| December 4, 2024 | [Mars Perps](https://github.com/oak-security/audit-reports/blob/main/Mars/2024-12-04%20Audit%20Report%20-%20Mars%20Perps%20v1.0.pdf) | 2 | 3 | 2 | 3 | 10 |
| **Total** | **11 reports** | **16** | **26** | **50** | **57** | **149** |

## 2022-02-17 — Mars

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Mars/2022-02-17%20Audit%20Report%20-%20Mars%20v1.0.pdf) · February 17, 2022 · 14 findings (5 critical, 0 major, 7 minor, 2 informational)

**Scope.** The audit has been performed on the following GitHub repository: https://github.com/mars-protocol/mars-core Commit hash: 94183e9555122a5cdfc8ca967e190215f61f8726.

**Notable findings**

- **Critical** — Deactivated market assets would cause forced liquidation on borrowers — *Acknowledged*
- **Critical** — Staking xMars rewards can be sandwiched by an attacker, skimming its value before accruing to stakers — *Acknowledged*
- **Critical** — Malicious smart contracts can avoid liquidation attempts — *Resolved*
- **Critical** — Disabled collateral assets can be liquidated — *Resolved*
- **Critical** — Incorrect slashing calculation will lead to loss of user funds — *Resolved*

## 2022-02-17 — Mars Periphery

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Mars/2022-02-17%20Audit%20Report%20-%20Mars%20Periphery%20v1.0.pdf) · February 17, 2022 · 8 findings (0 critical, 1 major, 5 minor, 2 informational)

**Scope.** The audit has been performed on the following GitHub repository: https://github.com/mars-protocol/mars-periphery Commit hash: 130c3c600f16ce7e751d769a4699f96fa5eda61e.

**Notable findings**

- **Major** — Users are unable to withdraw funds once admin deposited all funds in the Red Bank — *Resolved*

## 2022-02-17 — Fields of Mars

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Mars/2022-02-17%20Audit%20Report%20-%20Fields%20of%20Mars%20v1.0.pdf) · February 17, 2022 · 8 findings (0 critical, 1 major, 4 minor, 3 informational)

**Scope.** The audit has been performed on the following GitHub repository: https://github.com/mars-protocol/fields-of-mars Commit hash: 386ffc7c0aebdac0c7402aca01af34466c6bee9b.

**Notable findings**

- **Major** — Harvest message can be sandwiched to skim rewards — *Resolved*

## 2022-12-09 — Mars Rover

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Mars/2022-12-09%20Audit%20Report%20-%20Mars%20Rover%20v1.0.pdf) · December 9, 2022 · 16 findings (1 critical, 1 major, 6 minor, 8 informational)

**Scope.** The audit has been performed on the following GitHub repository: https://github.com/mars-protocol/rover Commit hash: 1c10aa538eaa1c2dc93f10faba6223b2eaed3ec6.

**Notable findings**

- **Critical** — Borrowers can prevent liquidation leading to bad debt accumulating — *Resolved*
- **Major** — Liquidators can extract a higher value by looping small amounts of liquidations — *Resolved*

## 2023-01-13 — Mars Outposts

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Mars/2023-01-13%20Audit%20Report%20-%20Mars%20Outposts%20v1.0.pdf) · January 13, 2023 · 21 findings (1 critical, 3 major, 10 minor, 7 informational)

**Scope.** The audit has been performed on the following GitHub repository: https://github.com/mars-protocol/outposts Commit hash: 62666cc07627ff41acda7196ca34ad8dbc1f1f8d.

**Notable findings**

- **Critical** — Disabled collateral can be re-enabled by depositing on behalf of the user — *Resolved*
- **Major** — Swapping assets in the reward collector contract are vulnerable to sandwich attack — *Resolved*
- **Major** — Red bank’s markets with an id greater than 128 cannot be used — *Resolved*
- **Major** — Incorrect refund address during debt repayment — *Resolved*

## 2023-02-03 — Mars Periphery

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Mars/2023-02-03%20Audit%20Report%20-%20Mars%20Periphery%20v1.0.pdf) · February 3, 2023 · 13 findings (1 critical, 2 major, 3 minor, 7 informational)

**Scope.** The audit has been performed on the following GitHub repository: https://github.com/mars-protocol/periphery Commit hash: 6b08edfd521c9b455b49eeb1b2e3329373636060.

**Notable findings**

- **Critical** — Liquidated and excess funds are stuck in the liquidation filterer contract — *Resolved*
- **Major** — Liquidation filterer contract cannot process multiple liquidations efficiently — *Resolved*
- **Major** — Smart contracts holding tokens on Terra classic cannot claim their airdrop — *Acknowledged*

## 2023-02-03 — Mars Rover Updates

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Mars/2023-02-03%20Audit%20Report%20-%20Mars%20Rover%20Updates%20v1.0.pdf) · February 3, 2023 · 9 findings (0 critical, 2 major, 1 minor, 6 informational)

**Scope.** The audit has been performed on the following GitHub repository: https://github.com/mars-protocol/rover Commit hash: d58f03cbdeeacc87226526b5e7c202ab989883d9.

**Notable findings**

- **Major** — Vault deposits are not affected by delisted coins — *Resolved*
- **Major** — account-nft’s contract UpdateConfig message cannot be executed after the minter role is transferred to credit-manager — *Resolved*

## 2023-08-01 — Mars Red Bank Updates

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Mars/2023-08-01%20Audit%20Report%20-%20Mars%20Red%20Bank%20Updates%20v1.0.pdf) · August 1, 2023 · 14 findings (3 critical, 4 major, 5 minor, 2 informational)

**Scope.** Repository https://github.com/mars-protocol/red-bank commit 7149f580bf6f7593d2ccaa4c09a2d63dc482d5ff. In the scope of this audit were all changes and their integration since our previous Mars Outposts audit, which was performed on commit 62666cc07627ff41acda7196ca34ad8dbc1f1f8d.

**Notable findings**

- **Critical** — Missing denom validation when adding incentives could lead to insufficient funds error — *Resolved*
- **Critical** — Incorrect calculation when simulating with multiple routes — *Resolved*
- **Critical** — Utilization rate can be exploited to surpass 100% for new markets — *Resolved*
- **Major** — Removing whitelisted denoms causes leftover rewards to get stuck — *Acknowledged*
- **Major** — Owner cannot update minimum emission without consequences — *Resolved*
- **Major** — Updating base denom would cause incorrect price results — *Acknowledged*
- **Major** — Incentive rewards might be distributed to depositors outside the epoch period — *Acknowledged*

## 2023-09-14 — Mars Rover v2

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Mars/2023-09-14%20Audit%20Report%20-%20Mars%20Rover%20v2%20v1.0.pdf) ·  · 21 findings (1 critical, 5 major, 6 minor, 9 informational)

**Scope.** Repository https://github.com/mars-protocol/rover commit 6013cbca21a343bbea695aac6b178c7be83948b2. This audit covers the changes since our previous audit, which was performed on commit d58f03cbdeeacc87226526b5e7c202ab989883d9 Identifier In this report, all paths pointing to this repository are prefixed with rover: Note …

Fixes verified at commit `3b7dbec0d2b4`.

**Notable findings**

- **Critical** — Lendings in the red bank cannot be liquidated when ActionKind::Default circuit breakers trigger — *Resolved*
- **Major** — Incorrect protocol fee calculation during liquidation — *Resolved*
- **Major** — Incorrect contract name assertion prevents successful migration — *Resolved*
- **Major** — Incomplete state migration in account-nft contract — *Resolved*
- **Major** — Circuit breakers may block liquidations, risking the protocol’s solvency — *Resolved*
- **Major** — Inaccurate health computation due to default collateral limit — *Resolved*

## 2024-07-15 — Mars v2 on Neutron

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Mars/2024-07-15%20Audit%20Report%20-%20Mars%20v2%20on%20Neutron%20v1.0.pdf) · July 15, 2024 · 15 findings (2 critical, 4 major, 1 minor, 8 informational)

**Scope.** Repository https://github.com/mars-protocol/contracts commit 3d59ad32e34ac64a821ddee5f5e3b017c04a7312. mars-oracle-wasm.

- contracts/oracle/wasm/src/price_source.rs
- contracts/oracle/wasm/src/lp_pricing.rs mars-credit-manager
- contracts/credit-manager/src/stake_astro_lp.rs
- contracts/credit-manager/src/unstake_astro_lp.r s
- contracts/credit-manager/src/claim_astro_lp_rew ards.rs
- contracts/credit-manager/src/liquidate_astro_lp .rs
- …and 14 further scope items.

**Notable findings**

- **Critical** — Total liquidity tokens are incorrectly increased, causing lower rewards — *Resolved*
- **Critical** — Attackers can bind vault account ID to forcefully cause a loss for users — *Resolved*
- **Major** — Liquidatee’s staking rewards are lost — *Resolved*
- **Major** — Users cannot stake new liquidity tokens on Astroport — *Resolved*
- **Major** — Potentially outdated configurations stored in the vault — *Resolved*
- **Major** — Incorrect liquidity tokens unstaked for ActionAmount::Exact — *Resolved*

## 2024-12-04 — Mars Perps

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Mars/2024-12-04%20Audit%20Report%20-%20Mars%20Perps%20v1.0.pdf) · December 4, 2024 · 10 findings (2 critical, 3 major, 2 minor, 3 informational)

**Scope.** Repository https://github.com/mars-protocol/core-contracts commit 60bed0b22e3fdb3bec4762c51053385a0c101529. This audit covers changes since our previous audit, which was performed at commit 01364db126c077abd6dc70799692de4551fc08d8. …

Fixes verified at commit `526798c0a2cb`.

**Notable findings**

- **Critical** — Incorrect migration guard unlock causes failed migration and loss of rewards — *Resolved*
- **Critical** — Users will lose accrued rewards when withdrawing liquidity — *Resolved*
- **Major** — Withdrawal may fail due to out-of-gas error when iterating positions — *Resolved*
- **Major** — Missing account ID validation allows removal of other user’s trigger orders — *Resolved*
- **Major** — Liquidation will fail for zero amounts — *Resolved*
