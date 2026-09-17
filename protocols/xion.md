# XION

Cosmos SDK, CosmWasm, JWT/passkeys · 3 published reports · 47 findings

Burnt's chain-level account abstraction: smart accounts authenticated with JWTs, passkeys and secp256k1/r1 keys, plus the supporting contracts.

**Role:** Reviewer across the contract and account-abstraction rounds.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| September 22, 2023 | [XION and Burnt Contracts](https://github.com/oak-security/audit-reports/blob/main/Burnt%20%28XION%29/2023-09-22%20Audit%20Report%20-%20XION%20and%20Burnt%20Contracts%20v1.1.pdf) | 4 | 4 | 1 | 6 | 15 |
| September 22, 2023 | [XION and Burnt Contract Updates and Account Abstraction](https://github.com/oak-security/audit-reports/blob/main/Burnt%20%28XION%29/2023-09-22%20Audit%20Report%20-%20XION%20and%20Burnt%20Contract%20Updates%20and%20Account%20Abstraction%20v1.1.pdf) | 0 | 1 | 4 | 14 | 19 |
| May 25, 2024 | [XION and Account Abstraction Updates 2](https://github.com/oak-security/audit-reports/blob/main/Burnt%20%28XION%29/2024-05-25%20Audit%20Report%20-%20XION%20and%20Account%20Abstraction%20Updates%202%20v1.0.pdf) | 0 | 1 | 7 | 5 | 13 |
| **Total** | **3 reports** | **4** | **6** | **12** | **25** | **47** |

## 2023-09-22 — XION and Burnt Contracts

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Burnt%20%28XION%29/2023-09-22%20Audit%20Report%20-%20XION%20and%20Burnt%20Contracts%20v1.1.pdf) · September 22, 2023 · 15 findings (4 critical, 4 major, 1 minor, 6 informational)

**Scope.** Repository https://github.com/burnt-labs/xion Identifier In this report, all paths pointing to this repository are prefixed with xion: commit 432e5d73e8bfc0e88de22dda206f405542ee7c91. All code in the repository was in scope. …

**Notable findings**

- **Critical** — check_ownable is incorrectly implemented which allows attackers to list any tokens — *Resolved*
- **Critical** — Anyone can lock any token_id — *Resolved*
- **Critical** — Anyone can halt any ongoing sale — *Resolved*
- **Critical** — buy_item will error when users supply the correct amount and denom — *Resolved*
- **Major** — Owner can be set to an invalid address — *Resolved*
- **Major** — Primary sales can be incorrectly configured — *Resolved*
- **Major** — Items can be bought from disabled or ended unlimited sales — *Resolved*
- **Major** — Wrong condition leads to disabled ongoing sales appearing as active — *Resolved*

## 2023-09-22 — XION and Burnt Contract Updates and Account Abstraction

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Burnt%20%28XION%29/2023-09-22%20Audit%20Report%20-%20XION%20and%20Burnt%20Contract%20Updates%20and%20Account%20Abstraction%20v1.1.pdf) · September 22, 2023 · 19 findings (0 critical, 1 major, 4 minor, 14 informational)

**Scope.** Repository https://github.com/burnt-labs/xion Reference This repository is referred to with the prefix xion: in all paths below. commit 3120374e88dbed49061c4794fe32cbfdb4252ab5. Only changes since our last audit, which was performed on commit 432e5d73e8bfc0e88de22dda206f405542ee7c91, were in scope. …

**Notable findings**

- **Major** — try_list poses centralization risk — *Resolved*

## 2024-05-25 — XION and Account Abstraction Updates 2

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Burnt%20%28XION%29/2024-05-25%20Audit%20Report%20-%20XION%20and%20Account%20Abstraction%20Updates%202%20v1.0.pdf) · May 25, 2024 · 13 findings (0 critical, 1 major, 7 minor, 5 informational)

**Scope.** Repository https://github.com/burnt-labs/xion commit a9bb0f5099f68474323ed8830c69b00130f8d91a. Only changes since our last audit, which was performed on commit 3120374e88dbed49061c4794fe32cbfdb4252ab5, were in scope. repository https://github.com/burnt-labs/contracts commit 91329a51b99d0322762266cc033112ee9f3e0471. …

**Notable findings**

- **Major** — Front-running audience creation opens phishing and other risks — *Resolved*
