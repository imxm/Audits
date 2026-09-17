# FairBlock

Cosmos SDK, identity-based encryption · 1 published report · 26 findings

fairyring: pre-execution privacy through identity-based encryption, with keyshare distribution and decryption keyed to block height.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| October 2, 2023 | [FairBlock fairyring](https://github.com/oak-security/audit-reports/blob/main/Fairblock/2023-10-02%20Audit%20Report%20-%20FairBlock%20fairyring%20v1.0.pdf) | 12 | 0 | 7 | 7 | 26 |

## 2023-10-02 — FairBlock fairyring

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Fairblock/2023-10-02%20Audit%20Report%20-%20FairBlock%20fairyring%20v1.0.pdf) · October 2, 2023 · 26 findings (12 critical, 0 major, 7 minor, 7 informational)

**Scope.** Repository https://github.com/fairblock/fairyring commit 46597175c7bfc588e732405cd518edfc717c8a17. All Cosmos SDK code in the app, cmd, and x directories was in scope.

**Notable findings**

- **Critical** — Attackers can register unbonded validators in the keyshare module to submit malicious key shares, censor, or DoS the chain — *Resolved*
- **Critical** — Attackers can register validators in the staking module to DoS the chain — *Resolved*
- **Critical** — Validators can censor the execution of encrypted transactions at a particular block height without being punished — *Resolved*
- **Critical** — Encrypted transaction execution does not charge gas — *Resolved*
- **Critical** — Attackers can overwrite legitimate AggregateKeyShares making the chain unable to execute transactions — *Resolved*
- **Critical** — Attackers can submit a large number of MsgSubmitEncryptedTx targeting the same block height to DoS the chain — *Resolved*
- **Critical** — Attackers can submit a transaction with a large number of MsgCreateAggregatedKeyShare messages to DoS the chain — *Resolved*
- **Critical** — Logged/emitted keys combined with ability to aggregate keys for future block heights allows decryption of transactions — *Resolved*
- …and 4 further critical/major findings in the report.
