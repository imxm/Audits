# Mantra Chain

Cosmos SDK · 1 published report · 33 findings

MANTRA Chain v5.0.0: the chain upgrade reviewed in phases.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| November 3, 2025 | [MANTRA Chain v5.0.0 Phases 1-3](https://github.com/oak-security/audit-reports/blob/main/MANTRA/2025-11-03%20Audit%20Report%20-%20MANTRA%20Chain%20v5.0.0%20Phases%201-3%20v1.3.pdf) | 2 | 1 | 12 | 18 | 33 |

## 2025-11-03 — MANTRA Chain v5.0.0 Phases 1-3

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/MANTRA/2025-11-03%20Audit%20Report%20-%20MANTRA%20Chain%20v5.0.0%20Phases%201-3%20v1.3.pdf) · November 3, 2025 · 33 findings (2 critical, 1 major, 12 minor, 18 informational)

**Scope.** The audit has been performed in multiple phases on the following targets: Phase 1 repository https://github.com/MANTRA-Chain/mantrachain. the changes applied in the following git diff.

- https://github.com/MANTRA-Chain/mantrachain/compare/v1.0.0...1a ec224716e1f14dfcde07e7b0d125444f0f8584 with tag v1.0.0 at commit 4e6cfdee274df38885e859201d2860c98d076165. …
- https://github.com/MANTRA-Chain/mantrachain/compare/1aec2247 16e1f14dfcde07e7b0d125444f0f8584...bd389403f26ee41a0d1cf8f5 7fef79a78106db58 Phase 3 Repos

Fixes verified at commit `3f144706adf7`.

**Notable findings**

- **Critical** — Module accounts are not blocked from receiving bank coins, resulting in a denial-of-service — *Resolved*
- **Critical** — Overwriting the tokenfactory hook call's gas meter with a fixed gas amount allows for a denial-of-service attack — *Resolved*
- **Major** — ProxyGasMeter allows for uncharged computation when the gas limit is exceeded or an overflow occurs — *Resolved*
