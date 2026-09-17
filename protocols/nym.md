# Nym

CosmWasm · 1 published report · 19 findings

Mixnet and vesting contracts: node bonding, delegation rewards and the vesting account logic.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| March 27, 2023 | [Nym Mixnet and Vesting Contracts](https://github.com/oak-security/audit-reports/blob/main/Nym/2023-03-27%20Audit%20Report%20-%20Nym%20Mixnet%20and%20Vesting%20Contracts%20v1.0.pdf) | 7 | 2 | 7 | 3 | 19 |

## 2023-03-27 — Nym Mixnet and Vesting Contracts

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Nym/2023-03-27%20Audit%20Report%20-%20Nym%20Mixnet%20and%20Vesting%20Contracts%20v1.0.pdf) · March 27, 2023 · 19 findings (7 critical, 2 major, 7 minor, 3 informational)

**Scope.** The audit has been performed on the following GitHub repository: https://github.com/nymtech/nym/ Commit hash: d9b682310669658756df974ef3e74c63cf4e7c70 The scope of this audit is limited to the following directories: - contracts/mixnet - contracts/vesting - relevant imports by these contracts.

**Notable findings**

- **Critical** — A failing epoch or interval event execution permanently blocks epoch advancement — *Acknowledged*
- **Critical** — Attackers can force orphan mixnodes to join a family without their consent in order to aggregate a large quantity of them in the same layer — *Resolved*
- **Critical** — Unbounded iteration in TrackUndelegation message handling could make the user unable to undelegate, which also permanently inhibits epoch advancement — *Resolved*
- **Critical** — An attacker could frontrun BondMixnodeOnBehalf and CreateFamilyOnBehalf messages and modify their payload — *Resolved*
- **Critical** — Signatures can be replayed within “on behalf” transactions in order to impersonate users — *Resolved*
- **Critical** — Key generation for (owner, proxy) pairs could lead to collisions — *Resolved*
- **Critical** — track_delegation can overwrite existing delegation if more than one is processed within the same block — *Resolved*
- **Major** — Bond owner is not able to control their bond if it was created “on behalf” by a proxy — *Acknowledged*
- …and 1 further critical/major findings in the report.
