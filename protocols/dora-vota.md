# Dora Vota

Cosmos SDK, CosmWasm, Solidity · 2 published reports · 17 findings

Dora Factory's quadratic-funding chain: the vota chain modules and the contract migration path.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| June 13, 2024 | [Dora Vota](https://github.com/oak-security/audit-reports/blob/main/DoraFactory/2024-06-13%20Audit%20Report%20-%20Dora%20Vota%20v1.0.pdf) | 1 | 4 | 1 | 1 | 7 |
| September 23, 2024 | [Dora Vota Migration Contract](https://github.com/oak-security/audit-reports/blob/main/DoraFactory/2024-09-23%20Audit%20Report%20-%20Dora%20Vota%20Migration%20Contract%20v1.0.pdf) | 0 | 1 | 3 | 6 | 10 |
| **Total** | **2 reports** | **1** | **5** | **4** | **7** | **17** |

## 2024-06-13 — Dora Vota

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/DoraFactory/2024-06-13%20Audit%20Report%20-%20Dora%20Vota%20v1.0.pdf) · June 13, 2024 · 7 findings (1 critical, 4 major, 1 minor, 1 informational)

**Scope.** Repository https://github.com/DoraFactory/doravota commit 0dae08469da2bcb021d85ce2ab83d5abd50645c9. All the code related to the baseapp was in scope.

Fixes verified at commit `e1e8c7bd251a`.

**Notable findings**

- **Critical** — Infinite gas allocated per block allows attackers to halt the chain — *Acknowledged*
- **Major** — Inconsistency between evidence and staking parameters allows malicious validators to escape penalties — *Acknowledged*
- **Major** — Usage of deprecated x/crisis module allows attackers to execute DoS attacks — *Acknowledged*
- **Major** — Oversized maximum block size could allow DoS attacks — *Acknowledged*
- **Major** — Vulnerability in wasmvm package — *Resolved*

## 2024-09-23 — Dora Vota Migration Contract

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/DoraFactory/2024-09-23%20Audit%20Report%20-%20Dora%20Vota%20Migration%20Contract%20v1.0.pdf) · September 23, 2024 · 10 findings (0 critical, 1 major, 3 minor, 6 informational)

**Scope.** Repository https://github.com/DoraFactory/dora-bridge-contract commit d92b30a5f46789f5dc3a35925aa0a264fb4ceb75. the contracts/DoraBridge.sol contract.

Fixes verified at commit `84117ea2a1df`.

**Notable findings**

- **Major** — Potential loss of funds due to missing address validation in submit function — *Acknowledged*
