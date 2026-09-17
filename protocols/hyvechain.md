# Hyvechain

Cosmos SDK, EVM precompiles · 1 published report · 55 findings

Hyvechain precompiles: the EVM precompile surface exposed over native chain modules.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| May 15, 2026 | [Hyvechain precompiles](https://github.com/oak-security/audit-reports/blob/main/Hyvechain%20precompiles/2026-05-15%20Audit%20Report%20-%20Hyvechain%20precompiles%20v1.0.pdf) | 6 | 15 | 28 | 6 | 55 |

## 2026-05-15 — Hyvechain precompiles

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Hyvechain%20precompiles/2026-05-15%20Audit%20Report%20-%20Hyvechain%20precompiles%20v1.0.pdf) · May 15, 2026 · 55 findings (6 critical, 15 major, 28 minor, 6 informational)

**Scope.** Repository https://github.com/hyveblockchain-dev/HYVECHAIN commit 3735553de794d600ce7d32cf8fb8e7bcc8b6f129. The scope of the audit was restricted to the .go files in the following directory.

- precompiles/masp/*
- precompiles/stealth/*
- precompiles/settlement/*
- precompiles/darkpool/*

Fixes verified at commit `c5743f4fc931`.

**Notable findings**

- **Critical** — TWAP records are never pruned, allowing chain halt via submit-then-cancel spam — *Resolved*
- **Critical** — Unshield validation does not bind amounts or recipients to the ZK proof, allowing full pool drainage — *Resolved*
- **Critical** — SubmitOrder accepts arbitrary orders without verifying the caller’s solvency or escrowing tokens — *Resolved*
- **Critical** — Stealth address generation uses broken cryptography — *Resolved*
- **Critical** — Shield path produces no shielded note, leaving the privacy module structurally non-functional — *Resolved*
- **Critical** — Convert anchor is unbound, allowing a prover to mint shielded staking rewards and airdrop tokens at arbitrary multipliers — *Resolved*
- **Major** — DarkPool precompile does not populate order.Commitment, causing all of a user's orders to share one nullifier — *Resolved*
- **Major** — ExpireRFQs scans every RFQ every block — *Resolved*
- …and 13 further critical/major findings in the report.
