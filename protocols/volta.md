# Volta

CosmWasm, Soroban · 2 published reports · 23 findings

Multisig wallet contracts, first on CosmWasm and then the Soroban port.

**Role:** Reviewer on both rounds.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| September 18, 2024 | [Volta CosmWasm](https://github.com/oak-security/audit-reports/blob/main/Volta/2024-09-18%20Audit%20Report%20-%20Volta%20CosmWasm%20v1.0.pdf) | 0 | 3 | 3 | 7 | 13 |
| November 19, 2025 | [Volta Soroban](https://github.com/oak-security/audit-reports/blob/main/Volta/2025-11-19%20Audit%20Report%20-%20Volta%20Soroban.pdf) | 0 | 1 | 3 | 6 | 10 |
| **Total** | **2 reports** | **0** | **4** | **6** | **13** | **23** |

## 2024-09-18 — Volta CosmWasm

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Volta/2024-09-18%20Audit%20Report%20-%20Volta%20CosmWasm%20v1.0.pdf) · September 18, 2024 · 13 findings (0 critical, 3 major, 3 minor, 7 informational)

**Scope.** Repository https://github.com/VoltaHQ/smart-contract-cosmwasm commit a5c6f5d916bfad53d977ba679a0c1f4e45c086fe. All contracts were in scope.

Fixes verified at commit `88af26a937ec`.

**Notable findings**

- **Major** — Incorrect vote logic prevents correct proposal processing — *Resolved*
- **Major** — Malicious owners or users spamming messages could prevent the admin from executing ProposalType::Configuration proposals — *Resolved*
- **Major** — Griefing risk due to unlimited fee grant allowance — *Resolved*

## 2025-11-19 — Volta Soroban

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Volta/2025-11-19%20Audit%20Report%20-%20Volta%20Soroban.pdf) · November 19, 2025 · 10 findings (0 critical, 1 major, 3 minor, 6 informational)

**Scope.** Repository https://github.com/VoltaHQ/smart-contract-soroban commit 0d7f14c6bc3eb341fc623a2cd851e63a3f20f119. All contracts were in scope.

Fixes verified at commit `042692c483dc`.

**Notable findings**

- **Major** — Premature proposal rejection due to incorrect threshold comparison logic — *Resolved*
