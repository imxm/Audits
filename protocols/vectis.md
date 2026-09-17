# Vectis

CosmWasm · 1 published report · 21 findings

Smart-contract wallet with guardians, relayed transactions and plugin extensions.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| March 14, 2024 | [Vectis](https://github.com/oak-security/audit-reports/blob/main/Vectis/2024-03-14%20Audit%20Report%20-%20Vectis%20v1.0.pdf) | 0 | 4 | 12 | 5 | 21 |

## 2024-03-14 — Vectis

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Vectis/2024-03-14%20Audit%20Report%20-%20Vectis%20v1.0.pdf) · March 14, 2024 · 21 findings (0 critical, 4 major, 12 minor, 5 informational)

**Scope.** Repository https://github.com/nymlab/vectis commit 1902fe863e786ac87d17f69f8ac3a0da1f54871e. All contracts were in scope. repository https://github.com/nymlab/vectis-contracts commit 47e6a9113ee284264db0ca623e006806b3f35afb. All contracts were in scope. …

**Notable findings**

- **Major** — Wallet fees can be circumvented — *Resolved*
- **Major** — Full-featured wallet creation may run out of gas — *Acknowledged*
- **Major** — Malfunctioning or malicious plugins could make the proxy contract unusable — *Resolved*
- **Major** — It is not possible to downgrade the subscription to the Free tier — *Resolved*
