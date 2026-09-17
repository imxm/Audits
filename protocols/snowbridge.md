# Snowbridge

Rust, Polkadot to Ethereum bridge · 1 published report · 10 findings

Trustless Polkadot to Ethereum bridge. My round covered the Fiat-Shamir transform applied to the BEEFY light-client verification.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| December 29, 2025 | [Snowbridge Fiat Shamir Beefy Changes](https://github.com/oak-security/audit-reports/blob/main/Snowbridge/2025-12-29%20Audit%20Report%20-%20Snowbridge%20Fiat%20Shamir%20Beefy%20Changes%20v1.0.pdf) | 1 | 0 | 1 | 8 | 10 |

## 2025-12-29 — Snowbridge Fiat Shamir Beefy Changes

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Snowbridge/2025-12-29%20Audit%20Report%20-%20Snowbridge%20Fiat%20Shamir%20Beefy%20Changes%20v1.0.pdf) · December 29, 2025 · 10 findings (1 critical, 0 major, 1 minor, 8 informational)

**Scope.** Repository https://github.com/Snowfork/snowbridge. the changes applied in the following pull requests.

- https://github.com/Snowfork/snowbridge/pull/1462 reviewed at commit 206278d9497e93ff5a4b3d2a0c4232ffc40d88b3, base branch at cbe15bb773bb871b80d49887e1848d5dbaae0dd9

Fixes verified at commit `a17220c7c14f`.

**Notable findings**

- **Critical** — Fiat-Shamir subsampling does not guarantee the inclusion of any honest validator — *Resolved*
