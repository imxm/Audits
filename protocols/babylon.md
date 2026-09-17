# Babylon

Cosmos SDK, Bitcoin timestamping, EOTS · 1 published report · 44 findings

Bitcoin staking protocol: BTC checkpointing, finality providers, extractable one-time signatures (EOTS) and the incentive module.

**Role:** Reviewer on the v1.1 to v2 upgrade audit.

## Reports

| Date | Report | Critical | Major | Minor | Info | Total |
|---|---|---|---|---|---|---|
| June 12, 2025 | [Babylon](https://github.com/oak-security/audit-reports/blob/main/Babylon/2025-06-12%20Audit%20Report%20-%20Babylon%20v1.0.pdf) | 0 | 3 | 26 | 15 | 44 |

## 2025-06-12 — Babylon

[Report PDF](https://github.com/oak-security/audit-reports/blob/main/Babylon/2025-06-12%20Audit%20Report%20-%20Babylon%20v1.0.pdf) · June 12, 2025 · 44 findings (0 critical, 3 major, 26 minor, 15 informational)

**Scope.** Repository https://github.com/babylonlabs-io/babylon path prefix babylon.

- The changes applied between v1.1.x and v2.x in https://github.com/babylonlabs-io/babylon/compare/release/v1.1.x...release/v2.x, reviewed at commit 00763782f728b8a5d4c96d50d3c49be76e33b13b, base branch at f0a29d60f206268b …
- The x/incentive module reviewed at commit d95f863e44cd9c0f8279e04e204da60b1112b070 repository https://github.com/babylonlabs-io/finality-provider path prefix finality-provider:. …
- https://github.com/babylonlabs-io/finality-provider/pull/462 reviewed at commit 32eea898b7627706af954db33003de9419d626c9, base branch at 6bc3ef37e07b6a1ffe468ce6f9f5c66bd79a9c61. Fixes verified

Fixes verified at commit `3da7d458efdd`.

**Notable findings**

- **Major** — Missing TLS credentials and HMAC key in gRPC client enables credential compromise and MITM attacks — *Resolved*
- **Major** — Retrieving staking transactions using incorrect page increments results in skipped transactions — *Resolved*
- **Major** — Missing message size enforcement in DeliverTx enables oversized IBC messages payload injection — *Resolved*
