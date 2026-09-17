# Zigchain

Cosmos SDK · 2 published reports · 54 findings

Zigchain's core modules over several rounds, reviewed diff-aware between releases.

**Role:** Reviewer.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| December 19, 2025 | [ZIGChain Update](https://github.com/oak-security/audit-reports/blob/main/ZIGChain/2025-12-19%20Audit%20Report%20-%20ZIGChain%20Update.pdf) | 1 | 0 | 1 | 7 | 9 |
| May 15, 2026 | [ZIGChain](https://github.com/oak-security/audit-reports/blob/main/ZIGChain/2026-05-15%20Audit%20Report%20%E2%80%93%20ZIGChain.pdf) | 1 | 8 | 21 | 15 | 45 |
| **Total** | **2 reports** | **2** | **8** | **22** | **22** | **54** |

## 2025-12-19 — ZIGChain Update

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/ZIGChain/2025-12-19%20Audit%20Report%20-%20ZIGChain%20Update.pdf) · December 19, 2025 · 9 findings (1 critical, 0 major, 1 minor, 7 informational)

**Scope.** Repository https://github.com/ZIGChain/zigchain-private commit ee96e9b83d488b6540a9c80cd3614b83a1876666. Updates since the last audit performed by Oak Security, which was conducted at commit 18a9e5d1a42dc9564be09b6feb2e6dbf2f40983e.

Fixes verified at commit `fe817f66275e`.

**Notable findings**

- **Critical** — Sent tokens are not refunded when the IBC counterpart fails — *Resolved*

## 2026-05-15 — ZIGChain

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/ZIGChain/2026-05-15%20Audit%20Report%20%E2%80%93%20ZIGChain.pdf) · May 15, 2026 · 45 findings (1 critical, 8 major, 21 minor, 15 informational)

**Scope.** Repository https://github.com/ZIGChain/zigchain-private commit cbcc293f6ac93d6de30c411f0193adbf857535f3. the following folders.

- app
- wasmbinding
- x Fixes verified at commit
- 73877afd31e0403664ef2877322dbfd2e7329367 (https://github.com/ZIGChain/zigchain-private)
- 1beec2759b759bf31fa5a3dcfd0d389e564fa3fb (https://github.com/ZIGChain/zigchain) The git tree hash of the private repository at commit 73877af (tag v4.0.0) is 0812f84f09f3a51633449dae23b8044a9dc9b828. …

**Notable findings**

- **Critical** — Pool transfer ante handler is bypassable via authz grants and CosmWasm contract execution — *Resolved*
- **Major** — RecoverZig lacks module address and vesting account blocklists — *Resolved*
- **Major** — DEX pool funds are sendable to blocked module addresses via the receiver parameter — *Resolved*
- **Major** — Missing ClaimDenomAdmin handler in CosmWasm message plugin — *Resolved*
- **Major** — AddLiquidity returns excess deposit coins to the receiver instead of the original sender — *Resolved*
- **Major** — Denial of service on fee withdrawal via unbounded balance iteration on factory module account — *Resolved*
- **Major** — Denial of service on liquidity removal via unbounded balance iteration on pool addresses — *Resolved*
- **Major** — Improper error handling in OnAcknowledgementPacket causes irrecoverable silent fund loss — *Resolved*
- …and 1 further critical/major findings in the report.
