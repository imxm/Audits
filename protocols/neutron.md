# Neutron

Cosmos SDK, Go, CosmWasm hooks · 1 published report · 67 findings

Neutron's migration from an Interchain Security consumer chain to an independent chain: staking, slashing, revenue and the CosmWasm hook surface.

**Role:** Reviewer on the independent-chain audit.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| March 25, 2025 | [Neutron Independent Chain](https://github.com/oak-security/audit-reports/blob/main/Neutron/2025-03-25%20Audit%20Report%20-%20Neutron%20Independent%20Chain%20v1.0.pdf) | 2 | 12 | 21 | 32 | 67 |

## 2025-03-25 — Neutron Independent Chain

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Neutron/2025-03-25%20Audit%20Report%20-%20Neutron%20Independent%20Chain%20v1.0.pdf) · March 25, 2025 · 67 findings (2 critical, 12 major, 21 minor, 32 informational)

**Scope.** Phase 1 repository https://github.com/neutron-org/neutron-private commit 71f29e201d59cfebc67e70fd8fbde47d62ecef4f. Only the app/upgrades/sovereign directory was in the scope of the audit. repository https://github.com/neutron-org/neutron-private commit 6c74b900cf84fe859d77c82ee2d4676a19fe4b48. …

Fixes verified at commit `aaba49ce9312`.

**Notable findings**

- **Critical** — Unsupported staking hooks cause a denial of service — *Acknowledged*
- **Major** — Failure to handle BeforeDelegationRemoved hook leads to stake inconsistency — *Resolved*
- **Major** — Incorrect parameter passed during SudoMsg::AfterValidatorRemoved — *Resolved*
- **Major** — Potential incorrect delegation logic in StakeWithDrop — *Resolved*
- **Major** — Bypassing the embedded filesystem causes file I/O errors on non-build machines, causing a denial of service — *Resolved*
- **Major** — Blacklist feature does not account for block height, causing incorrect vote computation — *Resolved*
- **Major** — Unbounded validator iteration causes potential out-of-gas errors — *Resolved*
- **Critical** — Validators receive lesser rewards due to incorrect reward denom — *Resolved*
- …and 6 further critical/major findings in the report.
