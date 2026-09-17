# Autonomy Network

CosmWasm · 1 published report · 15 findings

Automation network on Osmosis: registry, executors and the limit-order integration.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| March 6, 2023 | [Autonomy Osmosis](https://github.com/oak-security/audit-reports/blob/main/Autonomy/2023-03-06%20Audit%20Report%20-%20Autonomy%20Osmosis%20v1.1.pdf) | 0 | 3 | 7 | 5 | 15 |

## 2023-03-06 — Autonomy Osmosis

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Autonomy/2023-03-06%20Audit%20Report%20-%20Autonomy%20Osmosis%20v1.1.pdf) · March 6, 2023 · 15 findings (0 critical, 3 major, 7 minor, 5 informational)

**Scope.** The audit has been performed on the following GitHub repository: https://github.com/Autonomy-Network/autonomy-osmosis-contracts Commit hash: 00f5679fe7a518c88d9a0e8b0e5c9d0b496b34d1 Fixes have been verified on the commit with the following hash: 02528b908b97c0a5548623972790df59122ddc5d.

**Notable findings**

- **Major** — Delays in the execution of UpdateExecutor transactions could temporarily inhibit the capability of the protocol to execute requests — *Resolved*
- **Major** — stakes vector could exceed the CosmWasm VM memory limit when loaded — *Resolved*
- **Major** — Unstake transactions are likely to fail if more than one of them is processed in the same block — *Acknowledged*
