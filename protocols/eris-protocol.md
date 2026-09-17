# Eris Protocol

CosmWasm, Terra · 1 published report · 19 findings

Liquid staking hub and vote-escrow contracts on Terra.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| February 15, 2023 | [Eris Protocol](https://github.com/oak-security/audit-reports/blob/main/Eris%20Protocol/2023-02-15%20Audit%20Report%20-%20Eris%20Protocol%20v1.0.pdf) | 1 | 3 | 5 | 10 | 19 |

## 2023-02-15 — Eris Protocol

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Eris%20Protocol/2023-02-15%20Audit%20Report%20-%20Eris%20Protocol%20v1.0.pdf) · February 15, 2023 · 19 findings (1 critical, 3 major, 5 minor, 10 informational)

**Scope.** Repository https://github.com/erisprotocol/contracts-terra Initial commit 9b0744dc6a2614d0582d12131816d4a9dfd4b0a0. The scope of this audit was limited to: - contracts/hub - contracts/amp-governance/voting_escrow.

Fixes verified at commit `e22a1a6721bc`.

**Notable findings**

- **Critical** — First depositor can be front-run for unfair profit causing direct losses — *Resolved*
- **Major** — Underflow upon slope calculation may lead to unreliable voting power — *Resolved*
- **Major** — reconcile_batches can underflow, blocking reconciliations — *Resolved*
- **Major** — ExtendLockAmount and DepositFor can be abused to briefly gain voting power cheaply — *Resolved*
