# Stellar Core

C++/Rust, Soroban · 2 published reports · 83 findings

Consensus-protocol upgrades to the reference Stellar validator: SCP, overlay, buckets, transaction application and the Soroban host pipeline.

**Role:** Reviewer on the protocol upgrade audits.

> One further Stellar Core report is not public yet.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| October 17, 2025 | [Stellar Core Protocol 23 Changes](https://github.com/oak-security/audit-reports/blob/main/Stellar/2025-10-17%20Audit%20Report%20-%20Stellar%20Core%20Protocol%2023%20Changes%20v1.0.pdf) | 2 | 1 | 35 | 43 | 81 |
| November 13, 2025 | [Stellar Core Protocol 24 Changes](https://github.com/oak-security/audit-reports/blob/main/Stellar/2025-11-13%20Audit%20Report%20-%20Stellar%20Core%20Protocol%2024%20Changes%20v1.0.pdf) | 0 | 0 | 1 | 1 | 2 |
| **Total** | **2 reports** | **2** | **1** | **36** | **44** | **83** |

## 2025-10-17 — Stellar Core Protocol 23 Changes

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Stellar/2025-10-17%20Audit%20Report%20-%20Stellar%20Core%20Protocol%2023%20Changes%20v1.0.pdf) · October 17, 2025 · 81 findings (2 critical, 1 major, 35 minor, 43 informational)

**Scope.** Repository https://github.com/stellar/stellar-core commit 9819d1b3bcfc13c60dcf88a948811fd2f96e7eef. Changes to the repository since commit 2d8d764cdb800235d8bc33286197bc64a875931b were reviewed, including an assessment of how these modifications were integrated into the existing codebase. …

- Overlay module
- Crypto module
- Database module
- Main module
- SCP module
- Utils module
- …and 17 further scope items.

**Notable findings**

- **Critical** — Deleted ledger entries not propagated to thread state in parallel execution — *Resolved*
- **Critical** — Missing application of transaction sorting results in incorrect execution order and ledger state divergence — *Resolved*
- **Major** — Unauthenticated Denial of Service via unsafe character handling in error messages — *Resolved*

## 2025-11-13 — Stellar Core Protocol 24 Changes

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Stellar/2025-11-13%20Audit%20Report%20-%20Stellar%20Core%20Protocol%2024%20Changes%20v1.0.pdf) · November 13, 2025 · 2 findings (0 critical, 0 major, 1 minor, 1 informational)

**Scope.** Repository https://github.com/stellar/stellar-core commit 0d7b4345de396ad4e8d7dcc4460ddc6feeb27b11. Changes to the repository since the previous review commit 9819d1b3bcfc13c60dcf88a948811fd2f96e7eef were reviewed, excluding src/ledger/P23HotArchiveFix.cpp.

Fixes verified at commit `46fb6e469bd4`.

No critical or major findings; the report is minor and informational only.
