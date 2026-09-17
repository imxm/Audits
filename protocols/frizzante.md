# Frizzante

CosmWasm · 1 published report · 14 findings

Frizzante core contracts.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| January 30, 2025 | [Frizzante Core Contracts](https://github.com/oak-security/audit-reports/blob/main/Frizzante/2025-01-30%20Audit%20Report%20-%20Frizzante%20Core%20Contracts%20v1.0.pdf) | 8 | 1 | 2 | 3 | 14 |

## 2025-01-30 — Frizzante Core Contracts

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Frizzante/2025-01-30%20Audit%20Report%20-%20Frizzante%20Core%20Contracts%20v1.0.pdf) · January 30, 2025 · 14 findings (8 critical, 1 major, 2 minor, 3 informational)

**Scope.** Repository https://github.com/frizzante-finance/core commit 566319a84653858d9aa68a045b1d88c84a76e1a9. The scope was restricted to the following directories.

- contracts/notional-pool
- contracts/yield-token
- contracts/router
- packages/balances
- packages/lazy-distribution
- packages/proto
- …and 2 further scope items.

**Notable findings**

- **Critical** — Incorrect calculation of user shares leads to disproportionate rewards — *Resolved*
- **Critical** — Shares are minted to the incorrect address — *Resolved*
- **Critical** — User rewards are not accrued before burning yield tokens — *Resolved*
- **Critical** — Missing division by zero validation allows attackers to break the standardized yield contract — *Resolved*
- **Critical** — Inflated standardized yield token balance causes incorrect reward distribution — *Resolved*
- **Critical** — Attackers can cause reward updates to fail due to excessive iteration — *Resolved*
- **Major** — Liquidity withdrawal may fail due to the sensitivity of the logit curve at its edges — *Resolved*
- **Critical** — Fees sent to the router contract can be stolen — *Resolved*
- …and 1 further critical/major findings in the report.
