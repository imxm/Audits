# Dymension

Cosmos SDK, Go · 4 published reports · 50 findings

RollApp settlement layer: the hub's rollapp/sequencer modules, the dymint client, virtual frontier contracts and a white-box RollApp pentest.

**Role:** Reviewer across the Point 0D and Point 1D streams.

> Three further Dymension reports are not public.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| March 8, 2024 | [Dymension Point 0D](https://github.com/oak-security/audit-reports/blob/main/Dymension/2024-03-08%20Audit%20Report%20-%20Dymension%20Point%200D%20v1.0.pdf) | 4 | 1 | 10 | 7 | 22 |
| April 30, 2024 | [Dymension Point 1D Stream 2_ Virtual Frontier Contract](https://github.com/oak-security/audit-reports/blob/main/Dymension/2024-04-30%20Audit%20Report%20-%20Dymension%20Point%201D%20Stream%202_%20Virtual%20Frontier%20Contract%20v1.1.pdf) | 0 | 0 | 4 | 0 | 4 |
| July 9, 2024 | [Dymension Point 1D Stream 3_ Dymint](https://github.com/oak-security/audit-reports/blob/main/Dymension/2024-07-09%20Audit%20Report%20-%20Dymension%20Point%201D%20Stream%203_%20Dymint%20v1.1.pdf) | 1 | 7 | 8 | 3 | 19 |
| August 13, 2024 | [Dymension Point 1D Stream 6_ RollApp White-box Pentest](https://github.com/oak-security/audit-reports/blob/main/Dymension/2024-08-13%20Audit%20Report%20-%20Dymension%20Point%201D%20Stream%206_%20RollApp%20White-box%20Pentest%20v1.1.pdf) | 0 | 0 | 1 | 4 | 5 |
| **Total** | **4 reports** | **5** | **8** | **23** | **14** | **50** |

## 2024-03-08 — Dymension Point 0D

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Dymension/2024-03-08%20Audit%20Report%20-%20Dymension%20Point%200D%20v1.0.pdf) · March 8, 2024 · 22 findings (4 critical, 1 major, 10 minor, 7 informational)

**Scope.** Repository https://github.com/dymensionxyz/dymension commit 32ab176c1452f8739936701d1679667933fcab2a. The application in the app and cmd directories, the streamer module in the x/streamer directory, and verifying that the x/delayedack, x/denommetadata, x/rollapp, and x/sequencer modules are correctly using the RollapsE …

Fixes verified at commit `001fe5c4158e`.

**Notable findings**

- **Critical** — The invariant checking the last stream ID will break over time, potentially causing the chain to halt — *Resolved*
- **Critical** — Unbounded loop in PowApprox can be exploited to halt the chain — *Resolved*
- **Critical** — MsgEthereumTx EVM messages can be nested within a MsgExec message to bypass Ante handlers and steal transaction fees or perform a Denial-of-Service attack — *Resolved*
- **Critical** — Directly sending funds to the txfees module can result in a denial-of-service — *Resolved*
- **Major** — EVM contract addresses squatting via the vesting module resulting in non-functioning contracts and inaccessible funds — *Resolved*

## 2024-04-30 — Dymension Point 1D Stream 2_ Virtual Frontier Contract

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Dymension/2024-04-30%20Audit%20Report%20-%20Dymension%20Point%201D%20Stream%202_%20Virtual%20Frontier%20Contract%20v1.1.pdf) · April 30, 2024 · 4 findings (0 critical, 0 major, 4 minor, 0 informational)

**Scope.** Repository https://github.com/dymensionxyz/ethermint commit 8cdb58f3d43b0504cad3ef8b9fba059f7d10f67c. The changes introduced in pull request #11 into commit 9940df7eaafad2ddddcb704366329b34d4970b16 were in scope. …

No critical or major findings; the report is minor and informational only.

## 2024-07-09 — Dymension Point 1D Stream 3_ Dymint

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Dymension/2024-07-09%20Audit%20Report%20-%20Dymension%20Point%201D%20Stream%203_%20Dymint%20v1.1.pdf) · July 9, 2024 · 19 findings (1 critical, 7 major, 8 minor, 3 informational)

**Scope.** Repository https://github.com/dymensionxyz/dymint commit 19f8877fe96fb8d3f8b08bd541033b0d9536c7ce. All contracts were in scope.

Fixes verified at commit `7290af6f0088`.

**Notable findings**

- **Critical** — Peer nodes could receive blocks that are not applied by the sequencer — *Resolved*
- **Major** — HTTP server misconfiguration allows Slowloris DoS attacks — *Resolved*
- **Major** — CONTINUATION frames flood vulnerability in x/net allows attackers to DoS the node — *Resolved*
- **Major** — Incorrect mempool initialization height leads to discarded transactions — *Resolved*
- **Major** — Submitting blocks to the data availability and settlement layer can result in a deadlock — *Resolved*
- **Major** — Invalid blocks can be received via p2p gossip, potentially preventing block syncing — *Resolved*
- **Major** — Non-atomic batch submission to data availability and settlement layers causes repayment for the same data and potential indefinite failure — *Resolved*
- **Major** — Applying blocks concurrently can lead to unexpected errors — *Resolved*

## 2024-08-13 — Dymension Point 1D Stream 6_ RollApp White-box Pentest

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Dymension/2024-08-13%20Audit%20Report%20-%20Dymension%20Point%201D%20Stream%206_%20RollApp%20White-box%20Pentest%20v1.1.pdf) · August 13, 2024 · 5 findings (0 critical, 0 major, 1 minor, 4 informational)

No critical or major findings; the report is minor and informational only.
