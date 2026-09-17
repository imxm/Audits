# Paxi Network

Cosmos SDK · 1 published report · 18 findings

Application-specific Cosmos SDK chain and its custom modules.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| November 1, 2025 | [Paxi Network](https://github.com/oak-security/audit-reports/blob/main/Paxi/2025-11-01%20Audit%20Report%20-%20Paxi%20Network.pdf) | 0 | 1 | 6 | 11 | 18 |

## 2025-11-01 — Paxi Network

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Paxi/2025-11-01%20Audit%20Report%20-%20Paxi%20Network.pdf) · November 1, 2025 · 18 findings (0 critical, 1 major, 6 minor, 11 informational)

**Scope.** Repository https://github.com/paxi-web3/paxi commit fa0651faa8d9d22961720fd6ddaa86548473c809. the following custom Cosmos SDK modules.

- x/custommint
- x/customstaking

Fixes verified at commit `236627a4a4d8`.

**Notable findings**

- **Major** — Rejection sampling may cause unbounded looping under skewed validator weights — *Resolved*
