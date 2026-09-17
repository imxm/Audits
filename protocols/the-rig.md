# The Rig

Fuel, Sway/Rust · 2 published reports · 33 findings

Liquid staking on Fuel, plus the follow-up round on the protocol updates.

**Role:** Reviewer on both rounds.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| July 1, 2025 | [The Rig](https://github.com/oak-security/audit-reports/blob/main/The%20Rig/2025-07-01%20Audit%20Report%20-%20The%20Rig%20v1.0.pdf) | 0 | 3 | 9 | 7 | 19 |
| October 1, 2025 | [The Rig Updates](https://github.com/oak-security/audit-reports/blob/main/The%20Rig/2025-10-01%20Audit%20Report%20-%20The%20Rig%20Updates%20v1.1.pdf) | 0 | 0 | 8 | 6 | 14 |
| **Total** | **2 reports** | **0** | **3** | **17** | **13** | **33** |

## 2025-07-01 — The Rig

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/The%20Rig/2025-07-01%20Audit%20Report%20-%20The%20Rig%20v1.0.pdf) · July 1, 2025 · 19 findings (0 critical, 3 major, 9 minor, 7 informational)

**Scope.** Repository https://github.com/Rig-Labs/the-rig commit 26bcde7b614e78f59dc9970f4f813a3fe85749f9. the contracts defined in.

- ignition/contracts/price_feed
- ignition/contracts/rig
- ethereum/src, excluding the vendor directory

Fixes verified at commit `df17d40f524c`.

**Notable findings**

- **Major** — Missing price staleness check may lead to incorrect stFUEL minting — *Resolved*
- **Major** — Strict deviation threshold prevents timely price corrections and enables arbitrage risks — *Acknowledged*
- **Major** — Premature round finalization undermines aggregation window and enables timing attacks — *Acknowledged*

## 2025-10-01 — The Rig Updates

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/The%20Rig/2025-10-01%20Audit%20Report%20-%20The%20Rig%20Updates%20v1.1.pdf) · October 1, 2025 · 14 findings (0 critical, 0 major, 8 minor, 6 informational)

**Scope.** Repository https://github.com/Rig-Labs/the-rig commit 26bcde7b614e78f59dc9970f4f813a3fe85749f9. the ignition/contracts/staking_migration directory. repository https://github.com/Rig-Labs/the-rig commit 82c3a289b302de8df13098f6860dd3102e8028fc. the changes applied in commit 82c3a289b302de8df13098f6860dd3102e8028fc.

Fixes verified at commit `daa19d427327`.

No critical or major findings; the report is minor and informational only.
