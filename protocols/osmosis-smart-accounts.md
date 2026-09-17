# Osmosis Smart Accounts

Cosmos SDK, Go · 1 published report · 8 findings

Osmosis authenticator framework: pluggable account authenticators evaluated in the ante handler.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| July 3, 2024 | [Osmosis Smart Accounts](https://github.com/oak-security/audit-reports/blob/main/Osmosis%20Labs/2024-07-03%20Audit%20Report%20-%20Osmosis%20Smart%20Accounts%20v1.0.pdf) | 0 | 1 | 1 | 6 | 8 |

## 2024-07-03 — Osmosis Smart Accounts

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Osmosis%20Labs/2024-07-03%20Audit%20Report%20-%20Osmosis%20Smart%20Accounts%20v1.0.pdf) · July 3, 2024 · 8 findings (0 critical, 1 major, 1 minor, 6 informational)

**Scope.** Repository https://github.com/osmosis-labs/osmosis commit 15566f1f2945a16af9243dd376ee58a0d691b66a. Only the x/smart-account module was in the scope of this audit.

Fixes verified at commit `04341160b108`.

**Notable findings**

- **Major** — Excessive transaction fees are incurred — *Resolved*
