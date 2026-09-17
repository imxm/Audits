# Levana

CosmWasm · 1 published report · 28 findings

Levana perpetual swaps: the perps market, liquidity pool and liquidation logic.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| May 3, 2022 | [Levana Perpetual Swaps](https://github.com/oak-security/audit-reports/blob/main/Levana/2022-05-03%20Audit%20Report%20-%20Levana%20Perpetual%20Swaps%20v1.0.pdf) | 3 | 7 | 9 | 9 | 28 |

## 2022-05-03 — Levana Perpetual Swaps

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Levana/2022-05-03%20Audit%20Report%20-%20Levana%20Perpetual%20Swaps%20v1.0.pdf) · May 3, 2022 · 28 findings (3 critical, 7 major, 9 minor, 9 informational)

**Scope.** The audit has been performed on the following GitHub repositories: https://github.com/Levana-Protocol/levana-perpetual-swap-contracts Commit hash: b44eba884752767720aca1d04e67fc137b8a7c7f https://github.com/Levana-Protocol/levana-common Commit hash: 5b1c2eeb2c633b486a19cfe401b2c32e461e723d.

**Notable findings**

- **Critical** — Anyone can whitelist a new vAMM or overwrite an existing one — *Partially resolved*
- **Critical** — Risk fund is not able to partially disburse creditors — *Acknowledged*
- **Critical** — saveSwapInstruction can be executed by anyone with arbitrary values — *Acknowledged*
- **Major** — assert_admin might run out of gas and contract-specific admins might lead to inconsistency and misconfiguration risks — *Resolved*
- **Major** — Risk fund is not aware of the fees sent from the vault — *Acknowledged*
- **Major** — is_vamm_addr might run out of gas — *Acknowledged*
- **Major** — Prices collected from oracle are inverted — *Resolved*
- **Major** — CollectFee message execution might run out of gas — *Acknowledged*
- …and 2 further critical/major findings in the report.
