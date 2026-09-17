# Router Protocol

Cosmos SDK, CosmWasm, Go, Solidity, NEAR, Solana · 9 published reports · 344 findings

Router chain and the Voyager stack: the chain's cross-chain modules, orchestrator, asset bridge, DexSpan aggregator and the EVM/NEAR gateway contracts.

**Role:** Lead across the chain, gateway and Voyager rounds.

> Five further Router reports are not public.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| November 27, 2022 | [Router](https://github.com/oak-security/audit-reports/blob/main/Router/2022-11-27%20Audit%20Report%20-%20Router%20v1.0.pdf) | 3 | 6 | 20 | 14 | 43 |
| April 29, 2024 | [Router Voyager Forwarder](https://github.com/oak-security/audit-reports/blob/main/Router/2024-04-29%20Audit%20Report%20-%20Router%20Voyager%20Forwarder%20v1.0.pdf) | 6 | 11 | 15 | 17 | 49 |
| April 30, 2024 | [Router Asset Bridge](https://github.com/oak-security/audit-reports/blob/main/Router/2024-04-30%20Audit%20Report%20-%20Router%20Asset%20Bridge%20v1.2.pdf) | 7 | 15 | 18 | 13 | 53 |
| April 30, 2024 | [Router Chain 2](https://github.com/oak-security/audit-reports/blob/main/Router/2024-04-30%20Audit%20Report%20-%20Router%20Chain%202%20v1.0.pdf) | 7 | 11 | 9 | 7 | 34 |
| April 30, 2024 | [Router Orchestrator](https://github.com/oak-security/audit-reports/blob/main/Router/2024-04-30%20Audit%20Report%20-%20Router%20Orchestrator%20v1.0.pdf) | 4 | 4 | 9 | 10 | 27 |
| April 30, 2024 | [Router Voyager Forwarder and CW Gateway](https://github.com/oak-security/audit-reports/blob/main/Router/2024-04-30%20Audit%20Report%20-%20Router%20Voyager%20Forwarder%20and%20CW%20Gateway%20v1.2.pdf) | 19 | 20 | 14 | 16 | 69 |
| May 10, 2024 | [Router DexSpan](https://github.com/oak-security/audit-reports/blob/main/Router/2024-05-10%20Audit%20Report%20-%20Router%20DexSpan%20v1.0.pdf) | 1 | 5 | 10 | 15 | 31 |
| May 29, 2024 | [Router EVM and NEAR Gateway Contracts and WASM Bindings](https://github.com/oak-security/audit-reports/blob/main/Router/2024-05-29%20Audit%20Report%20-%20Router%20EVM%20and%20NEAR%20Gateway%20Contracts%20and%20WASM%20Bindings%20v1.0.pdf) | 3 | 7 | 10 | 13 | 33 |
| May 29, 2024 | [Router Integration](https://github.com/oak-security/audit-reports/blob/main/Router/2024-05-29%20Audit%20Report%20-%20Router%20Integration%20v1.0.pdf) | 1 | 3 | 1 | 0 | 5 |
| **Total** | **9 reports** | **51** | **82** | **106** | **105** | **344** |

## 2022-11-27 — Router

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Router/2022-11-27%20Audit%20Report%20-%20Router%20v1.0.pdf) · November 27, 2022 · 43 findings (3 critical, 6 major, 20 minor, 14 informational)

**Notable findings**

- **Critical** — RouterCrossTalk: DoS by frontrunning with approving fees to a value of 0 — *Resolved*
- **Critical** — RouterERC20Upgradable.sol: Paused contract does not pause minting/burning — *Resolved*
- **Critical** — Static feeFactor allows economic attacks in certain market conditions, and leads to users overpaying in others — *Acknowledged*
- **Major** — Missing storage gaps for upgradeable contracts might lead to storage slot collisions — *Resolved*
- **Major** — Return value of transfer function not checked — *Acknowledged*
- **Major** — Failure to revoke permission of the previous owner — *Resolved*
- **Major** — Incorrect usage of initializer functions — *Resolved*
- **Major** — Missing external initializer of the RouterERC20Upgradable contract — *Acknowledged*
- …and 1 further critical/major findings in the report.

## 2024-04-29 — Router Voyager Forwarder

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Router/2024-04-29%20Audit%20Report%20-%20Router%20Voyager%20Forwarder%20v1.0.pdf) · April 29, 2024 · 49 findings (6 critical, 11 major, 15 minor, 17 informational)

**Scope.** Repository https://github.com/router-protocol/voyager-forwarder commit ad2e63969a72bd4195961fca6069738659a91f61. All files were in scope. Note that commented code has not been audited.

Fixes verified at commit `16a88a2ef40b`.

**Notable findings**

- **Critical** — Missing HTTP timeouts enable Slowloris DoS attacks — *Resolved*
- **Critical** — Improper usage of goroutines leads to memory and thread leaks as well as deadlocks — *Partially Resolved*
- **Critical** — Using BlockHeight instead of Timestamp calculates incorrect transaction expirations — *Resolved*
- **Critical** — NEAR eventProcessor disregards user configurations and forces the application to connect to untrusted nodes hosted on AWS — *Resolved*
- **Critical** — The isTransactionProfitable function always returns true leading the forwarder’s operator to relay transactions at a loss — *Resolved*
- **Critical** — Limitations in Network configuration and untrusted hardcoded endpoint usage — *Partially Resolved*
- **Major** — Improper error handling in Processor’s Start method stops forwarders’ operations — *Resolved*
- **Major** — SR25519 key generation requires an external untrusted binary — *Resolved*
- …and 9 further critical/major findings in the report.

## 2024-04-30 — Router Asset Bridge

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Router/2024-04-30%20Audit%20Report%20-%20Router%20Asset%20Bridge%20v1.2.pdf) · April 30, 2024 · 53 findings (7 critical, 15 major, 18 minor, 13 informational)

**Scope.** Repository https://github.com/router-protocol/asset-bridge-contracts commit 4fc1add571ea0525e8f1fac28ef8ced8d03894ca. All contracts were in the scope, excluding the test files and contracts inside the near/contracts/sequencer-staking directory.

Fixes verified at commit `6a2f6b3d7190`.

**Notable findings**

- **Critical** — Attackers can front-run transactions to steal user funds after approving allowances — *Resolved*
- **Critical** — Attackers can profit by depositing different tokens and withdrawing as native tokens — *Resolved*
- **Critical** — Attackers can register and deregister their accounts for profit — *Resolved*
- **Critical** — Inability to decode request packet payload due to incorrect indexes results in failed cross-chain requests — *Resolved*
- **Critical** — Refunding fails due to set_execute_revert_record function — *Resolved*
- **Critical** — NEAR tokens are incorrectly transferred to the gateway contract instead of being escrowed in the AssetBridge contract — *Resolved*
- **Critical** — Fungible token refunds will fail, causing a loss of funds for users — *Resolved*
- **Major** — Payable keyword is not specified on functions that expect funds to be sent — *Resolved*
- …and 14 further critical/major findings in the report.

## 2024-04-30 — Router Chain 2

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Router/2024-04-30%20Audit%20Report%20-%20Router%20Chain%202%20v1.0.pdf) · April 30, 2024 · 34 findings (7 critical, 11 major, 9 minor, 7 informational)

**Scope.** Repository https://github.com/router-protocol/router-chain commit f9ff8b44467d9d0b898b30726ffac421071d58e1. All modules in the x/ directory were in scope.

Fixes verified at commit `4f44e99c38ea`.

**Notable findings**

- **Critical** — Blocked cross-chain requests are indefinitely retried and could be exploited for denial-of-service attacks — *Resolved*
- **Critical** — Non-deterministic iteration in ClaimEventSlashing can cause consensus failure — *Resolved*
- **Critical** — Unapproved fee payers can block legitimate requests which can be exploited for denial-of-service attacks — *Resolved*
- **Critical** — Anyone can submit forged cross-chain requests — *Resolved*
- **Critical** — Anyone can submit forged cross-chain ack requests — *Resolved*
- **Critical** — Unbonding validators can circumvent slashing — *Resolved*
- **Critical** — Deactivated price feeders are not enforced — *Resolved*
- **Major** — Failed requests will not be reflected for ErrorGasOverflow panics — *Resolved*
- …and 10 further critical/major findings in the report.

## 2024-04-30 — Router Orchestrator

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Router/2024-04-30%20Audit%20Report%20-%20Router%20Orchestrator%20v1.0.pdf) · April 30, 2024 · 27 findings (4 critical, 4 major, 9 minor, 10 informational)

**Scope.** Repository https://github.com/router-protocol/router-orchestrator commit fee27164a82be6af1b366c1045ac09cc70b33827. All files were in scope.

Fixes verified at commit `34a84e26745a`.

**Notable findings**

- **Critical** — Events emitted from the EVM gateway and voyager contracts are potentially processed out of order, resulting in events being skipped and not sent to Router Chain — *Resolved*
- **Critical** — Inbound and outbound CROSSTALK requests originating from non-Cosmos chains are ignored and not able to be relayed — *Acknowledged*
- **Critical** — Transaction origin is hardcoded as an empty string when transforming an iSend event — *Resolved*
- **Critical** — A potential unconfirmed block is processed in the NEAR event listener — *Resolved*
- **Major** — Suboptimal processing of attestations leading to missing attestations — *Resolved*
- **Major** — Risk of liveness slashing due to inconsistent chain configurations — *Acknowledged*
- **Major** — Unhandled errors in the codebase — *Partially Resolved*
- **Major** — Incorrect gas price denom used — *Resolved*

## 2024-04-30 — Router Voyager Forwarder and CW Gateway

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Router/2024-04-30%20Audit%20Report%20-%20Router%20Voyager%20Forwarder%20and%20CW%20Gateway%20v1.2.pdf) · April 30, 2024 · 69 findings (19 critical, 20 major, 14 minor, 16 informational)

**Scope.** Repository https://github.com/router-protocol/asset-forwarder-contracts commit 47f8e3ce2edc333e1c063820d33812b2570e85dd. All contracts excluding the evm/src/dexspan/* directory were in scope. …

Fixes verified at commit `705e8febd4bf`.

**Notable findings**

- **Critical** — Incorrect reentrancy unlock causes denial of service — *Resolved*
- **Critical** — Attackers can create deposit requests without including funds — *Resolved*
- **Critical** — Unauthorized ibc_channel_connect may lead to unauthorized calls — *Resolved*
- **Critical** — Nonce is incorrectly incremented when fungible tokens transfer fails — *Resolved*
- **Critical** — Attackers can register and deregister their accounts for profit — *Resolved*
- **Critical** — Lowercasing case-sensitive addresses causes unexpected behavior and loss of funds — *Resolved*
- **Critical** — Incorrect tokens are used to account for claimable tokens, causing a loss of funds — *Resolved*
- **Critical** — Attackers can steal funds by repeatedly withdrawing blocked funds — *Resolved*
- …and 31 further critical/major findings in the report.

## 2024-05-10 — Router DexSpan

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Router/2024-05-10%20Audit%20Report%20-%20Router%20DexSpan%20v1.0.pdf) · May 10, 2024 · 31 findings (1 critical, 5 major, 10 minor, 15 informational)

**Scope.** Repository https://github.com/router-protocol/asset-forwarder-contracts commit 93dcff0884c3a03d2e18dfc0398d5d4e1f26046f. Only contracts in evm/src/dexspan were in scope.

Fixes verified at commit `144f352288fe`.

**Notable findings**

- **Critical** — Missing transaction revert could lead to loss of funds — *Acknowledged*
- **Major** — Contract upgradability is not properly implemented — *Resolved*
- **Major** — The UniswapV2’s skim address is hardcoded which may lead to a loss of funds on other chains — *Resolved*
- **Major** — Maximum approval on third-party components may lead to drain of funds — *Resolved*
- **Major** — DEX swap functions enable users to perform arbitrary calls — *Acknowledged*
- **Major** — Deposits in native currency always revert — *Resolved*

## 2024-05-29 — Router EVM and NEAR Gateway Contracts and WASM Bindings

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Router/2024-05-29%20Audit%20Report%20-%20Router%20EVM%20and%20NEAR%20Gateway%20Contracts%20and%20WASM%20Bindings%20v1.0.pdf) · May 29, 2024 · 33 findings (3 critical, 7 major, 10 minor, 13 informational)

**Scope.** Repository https://github.com/router-protocol/router-gateway-contracts commit e863130d284eb52c8c1a8fe8859f5495ee448853. Only the contracts in the evm/* and near/gateway-upgradeable/* directories were in the scope of the audit. …

Fixes verified at commit `6ecfda2fa2fe`.

**Notable findings**

- **Critical** — Incorrect isReadCall implementation allows infinite token mints — *Resolved*
- **Critical** — Duplicate IReceiveEvent event nonces in the NEAR gateway contract resulting in stuck cross-chain requests — *Resolved*
- **Critical** — ROUTE tokens are not minted for invalid requests, causing a loss of funds — *Resolved*
- **Major** — ASM contract state is committed when token mint fails — *Acknowledged*
- **Major** — Packet loss during iReceive execution due to updateValset transaction front-running — *Acknowledged*
- **Major** — Validator set supermajority threshold discrepancy between the gateway contracts and Router Chain — *Resolved*
- **Major** — Incomplete state rollback for failures in minting the ROUTE token — *Resolved*
- **Major** — Execution status is incorrectly set to success when the handler address cannot be parsed — *Resolved*
- …and 2 further critical/major findings in the report.

## 2024-05-29 — Router Integration

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Router/2024-05-29%20Audit%20Report%20-%20Router%20Integration%20v1.0.pdf) · May 29, 2024 · 5 findings (1 critical, 3 major, 1 minor, 0 informational)

**Scope.** During this audit phase, we conducted a thorough review of the entire lifecycle of requests going through the Router protocol. This lifecycle begins when a user initiates a cross-chain request on the source chain. …

**Notable findings**

- **Critical** — Failed cross-chain requests are repeatedly processed in Router Chain’s EndBlocker, potentially causing Denial-of-Service — *Resolved*
- **Major** — Malicious relayer can purposefully fail cross-chain requests on EVM destination chains — *Resolved*
- **Major** — Fee settlement can be bypassed for inbound and crosstalk requests, resulting in relayers not being compensated — *Resolved*
- **Major** — NEAR gateway contract does not allocate sufficient gas for handler calls — *Resolved*
