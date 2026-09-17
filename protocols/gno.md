# Gno

GnoVM, Go, Tendermint variant · 4 published reports · 91 findings

Gno.land's execution layer: GnoVM determinism and gas metering, the Gno standard library, and the Tendermint2 consensus fork.

**Role:** Reviewer across the sprint audits and the later updates round.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| January 17, 2025 | [Gno Sprint 1](https://github.com/oak-security/audit-reports/blob/main/Gno/2025-01-17%20Audit%20Report%20-%20Gno%20Sprint%201%20v1.0.pdf) | 3 | 6 | 7 | 17 | 33 |
| January 27, 2025 | [Gno Sprint 2](https://github.com/oak-security/audit-reports/blob/main/Gno/2025-01-27%20Audit%20Report%20-%20Gno%20Sprint%202%20v1.0.pdf) | 3 | 4 | 1 | 8 | 16 |
| March 25, 2025 | [Gno Sprint 3](https://github.com/oak-security/audit-reports/blob/main/Gno/2025-03-25%20Audit%20Report%20-%20Gno%20Sprint%203%20v1.0.pdf) | 0 | 0 | 9 | 8 | 17 |
| January 9, 2026 | [Gno Updates](https://github.com/oak-security/audit-reports/blob/main/Gno/2026-01-09%20Audit%20Report%20-%20Gno%20Updates%20v1.0.pdf) | 3 | 6 | 8 | 8 | 25 |
| **Total** | **4 reports** | **9** | **16** | **25** | **41** | **91** |

## 2025-01-17 — Gno Sprint 1

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Gno/2025-01-17%20Audit%20Report%20-%20Gno%20Sprint%201%20v1.0.pdf) · January 17, 2025 · 33 findings (3 critical, 6 major, 7 minor, 17 informational)

**Scope.** Repository https://github.com/gnolang/gno commit 88fb8cb3aac1e3b393a9f8e88304b78fbe1240da. The audit scope focuses on the interactions between components, smart contract injection risks, and specific example packages and realms within the GnoLand ecosystem.

- Interactions
- Assessment of the interaction between smart contracts (realms) and the GnoVM, focusing on the implementation of the VM Keeper
- Verification of operations executed at the end of blocks
- Assessment of the correctness and security of processes that update validator states
- Smart contract injection risks
- Assessment of mechanisms for deploying and executing smart contracts (realms). This includes the review of the following message handlers: ■ MsgAddPkg ■ MsgCall ■ MsgRun
- …and 2 further scope items.

**Notable findings**

- **Critical** — Attackers can craft malicious contracts and trigger a denial of service — *Reported*
- **Critical** — Attackers can abuse source code formatting to trigger a denial of service — *Reported*
- **Critical** — Lack of call stack depth limit could introduce non-determinism during machine execution — *Reported*
- **Major** — Unbounded resource usage in the queryEval function leads to a denial of service — *Reported*
- **Major** — Genesis signature verification is disabled in production environments — *Reported*
- **Major** — Potential memory overflow during package loading — *Reported*
- **Major** — Incorrect AVL tree balance condition causes degraded performance — *Reported*
- **Major** — Validators can be registered with unrelated addresses and public keys — *Reported*
- …and 1 further critical/major findings in the report.

## 2025-01-27 — Gno Sprint 2

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Gno/2025-01-27%20Audit%20Report%20-%20Gno%20Sprint%202%20v1.0.pdf) · January 27, 2025 · 16 findings (3 critical, 4 major, 1 minor, 8 informational)

**Scope.** Repository https://github.com/gnolang/gno commit 1b89166af37dd2ee63f5a30b81769532fd0bb1f7. The audit focuses on key components of the GnoVM ecosystem, including storage mechanisms, non-deterministic behavior, and virtual machine (VM) validity. Specific areas of interest include.

- Realm Storage
- Evaluation of functions and mechanisms related to realm updates and transaction finalization. This includes a review of the following files: ■ gnovm/pkg/gnolang/ownership.go ■ gnovm/pkg/gnolang/realm.go ■ gnovm/pkg/gnola …
- Non-Determinism
- We focused on key language features and their mapping to the underlying Go implementation to find non deterministic paths, specifically reviewing: ■ gnovm/pkg/gnolang/preprocess.go ■ gnovm/pkg/gnolang/values_string.go ■ …
- VM Validity
- Assessment of the validity and correctness of virtual machine operations, particularly in: ■ gnovm/pkg/gnolang/preprocess.go ■ gnovm/pkg/gnolang/go2gno.go

**Notable findings**

- **Critical** — Non-determinism in pointer address logging causes inconsistent block production — *Reported*
- **Critical** — Deleted objects are not correctly marked, causing memory leaks — *Reported*
- **Critical** — Insufficient gas metering and unmetered operations lead to denial of service — *Reported*
- **Major** — Memory leaks in Stringer methods affect node resource consumption — *Reported*
- **Major** — Read-only execution is not enforced due to an uninitialized field — *Reported*
- **Major** — Unbounded cache growth allows memory exhaustion attacks — *Reported*
- **Major** — Improper ObjectID parsing causes integer overflows and non-determinism — *Reported*

## 2025-03-25 — Gno Sprint 3

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Gno/2025-03-25%20Audit%20Report%20-%20Gno%20Sprint%203%20v1.0.pdf) · March 25, 2025 · 17 findings (0 critical, 0 major, 9 minor, 8 informational)

**Scope.** Repository https://github.com/gnolang/gno. the changes applied in the https://github.com/gnolang/gno/pull/3860 pull request reviewed at commit d24efa034173cb57168e27afdb3dcce4a07767fb, base branch at a5e084cc668cbd55eb324f2c8970b8e0aca2b584 in the following paths.

- examples/gno.land/r/sys/params
- gno.land/pkg/gnoland
- gno.land/pkg/sdk/vm
- gnovm/stdlibs/sys/params
- tm2/pkg/sdk/auth
- tm2/pkg/sdk/bank
- …and 2 further scope items.

No critical or major findings; the report is minor and informational only.

## 2026-01-09 — Gno Updates

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Gno/2026-01-09%20Audit%20Report%20-%20Gno%20Updates%20v1.0.pdf) · January 9, 2026 · 25 findings (3 critical, 6 major, 8 minor, 8 informational)

**Scope.** Repository https://github.com/gnolang/gno path prefix mempackage_type: commit 794907c9455aceb31f0abe42dee9b2ae35ffa8a4. the following files in the mempackage_type branch.

- gno/gnovm/pkg/gnolang/alloc.go
- gno/gnovm/pkg/gnolang/preprocess.go
- gnovm/pkg/gnolang/values_fill.go
- gnovm/pkg/gnolang/uverse.go:1060-1102 repository https://github.com/gnolang/gno path prefix pr_4060:. the changes applied in the following pull requests
- https://github.com/gnolang/gno/pull/4060 reviewed at commit fd67023b8a8520fffc1a3d5cb54d69b6dfca45f7, base branch at a3bffb2eb311cc27c419b519146a9906b5a82dba. …

**Notable findings**

- **Critical** — Insufficient gas metering and unmetered operations lead to denial of service — *Partially Resolved*
- **Critical** — Pass-by-value parameter in garbage collector nullifies gas accounting — *Resolved*
- **Critical** — ExpandWith omits memory accounting for wrapped values — *Resolved*
- **Major** — Underestimated CPU cycle cost for doOpReturnAfterCopy — *Acknowledged*
- **Major** — Unbounded recursion in Stacktrace serialization enables DoS — *Resolved*
- **Major** — Type checker bypass for data structures and interfaces — *Resolved*
- **Major** — Incorrect relations between interfaces can cause realm panics — *Resolved*
- **Major** — Garbage collector can exhaust the call stack and crash the node — *Resolved*
- …and 1 further critical/major findings in the report.
