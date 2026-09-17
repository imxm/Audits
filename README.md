# Audits

Security engagements where I was lead or a named reviewer, almost all delivered through
[Oak Security](https://oaksecurity.io). Reports are public in Oak's
[audit-reports](https://github.com/oak-security/audit-reports) repository. One row per protocol;
each protocol page lists its reports with scope, notable findings and links.

## Summary

- 29 protocols audited with Oak: 58 published reports, 1307 findings
- 138 critical, 215 major, 459 minor, 495 informational
- A further 22 reports are not public, plus 3 engagements delivered under NDA or another brand
- Stacks: Cosmos SDK and CosmWasm, Stellar Core and Soroban, GnoVM, Solana, NEAR, EVM, Polkadot bridge, Fuel
- Languages: Go, Rust, Solidity, C++ (read), Noir

`⁺` in the Reports column means further reports from that engagement are not public; the counts cover the published ones only.

## L1 core, consensus and VMs

| Protocol | Stack | Reports | Findings |
|---|---|---|---|
| [Stellar Core](protocols/stellar-core.md) | C++/Rust, Soroban | 2 ⁺ | 83 (2 critical, 1 major) |
| [Gno](protocols/gno.md) | GnoVM, Go, Tendermint variant | 4 | 91 (9 critical, 16 major) |
| [Neutron](protocols/neutron.md) | Cosmos SDK, Go, CosmWasm hooks | 1 | 67 (2 critical, 12 major) |
| [Babylon](protocols/babylon.md) | Cosmos SDK, Bitcoin timestamping, EOTS | 1 | 44 (3 major) |
| [Paxi Network](protocols/paxi-network.md) | Cosmos SDK | 1 | 18 (1 major) |
| [Dora Vota](protocols/dora-vota.md) | Cosmos SDK, CosmWasm, Solidity | 2 | 17 (1 critical, 5 major) |
| [XION](protocols/xion.md) | Cosmos SDK, CosmWasm, JWT/passkeys | 3 | 47 (4 critical, 6 major) |
| [Osmosis Smart Accounts](protocols/osmosis-smart-accounts.md) | Cosmos SDK, Go | 1 | 8 (1 major) |
| [FairBlock](protocols/fairblock.md) | Cosmos SDK, identity-based encryption | 1 | 26 (12 critical) |
| [Skip Protocol](protocols/skip-protocol.md) | Cosmos SDK, ABCI++ | 1 | 7 |
| [Zigchain](protocols/zigchain.md) | Cosmos SDK | 2 | 54 (2 critical, 8 major) |
| [Hyvechain](protocols/hyvechain.md) | Cosmos SDK, EVM precompiles | 1 | 55 (6 critical, 15 major) |
| [Agave (Solana validator client)](protocols/agave-solana.md) | Rust, Solana consensus | — | *Client under NDA; the report is not public* |

## Rollups, sequencers and settlement

| Protocol | Stack | Reports | Findings |
|---|---|---|---|
| [Fuel Sequencer](protocols/fuel-sequencer.md) | Cosmos SDK, CometBFT, Ethereum event ingestion | — | *12 reports / 73+ findings, per my engagement records* |
| [Dymension](protocols/dymension.md) | Cosmos SDK, Go | 4 ⁺ | 50 (5 critical, 8 major) |

## Cross-chain, bridges and relayers

| Protocol | Stack | Reports | Findings |
|---|---|---|---|
| [Router Protocol](protocols/router-protocol.md) | Cosmos SDK, CosmWasm, Go, Solidity, NEAR, Solana | 9 ⁺ | 344 (51 critical, 82 major) |
| [Snowbridge](protocols/snowbridge.md) | Rust, Polkadot to Ethereum bridge | 1 | 10 (1 critical) |
| [ICS721](protocols/ics721.md) | CosmWasm, IBC | 1 | 7 |

## Liquid staking and Bitcoin-linked

| Protocol | Stack | Reports | Findings |
|---|---|---|---|
| [The Rig](protocols/the-rig.md) | Fuel, Sway/Rust | 2 | 33 (3 major) |
| [Persistence / pSTAKE](protocols/persistence-pstake.md) | Go services, Cobo MPC, Solidity | 1 | 25 (6 critical, 3 major) |
| [Eris Protocol](protocols/eris-protocol.md) | CosmWasm, Terra | 1 | 19 (1 critical, 3 major) |

## DeFi

| Protocol | Stack | Reports | Findings |
|---|---|---|---|
| [Mars Protocol](protocols/mars-protocol.md) | CosmWasm | 11 | 149 (16 critical, 26 major) |
| [Levana](protocols/levana.md) | CosmWasm | 1 | 28 (3 critical, 7 major) |
| [Frizzante](protocols/frizzante.md) | CosmWasm | 1 | 14 (8 critical, 1 major) |
| [Autonomy Network](protocols/autonomy-network.md) | CosmWasm | 1 | 15 (3 major) |

## Wallets, multisig and account abstraction

| Protocol | Stack | Reports | Findings |
|---|---|---|---|
| [Volta](protocols/volta.md) | CosmWasm, Soroban | 2 | 23 (4 major) |
| [Vectis](protocols/vectis.md) | CosmWasm | 1 | 21 (4 major) |

## AI and verifiable compute

| Protocol | Stack | Reports | Findings |
|---|---|---|---|
| [AIxBlockchain](protocols/aixblockchain.md) | Verifiable inference | — | *Reports are not published yet* |

## Other

| Protocol | Stack | Reports | Findings |
|---|---|---|---|
| [Nym](protocols/nym.md) | CosmWasm | 1 | 19 (7 critical, 2 major) |
| [Spice Quest](protocols/spice-quest.md) | CosmWasm | — | *1 report / 18 findings, per my engagement records* |
| [Mantra Chain](protocols/mantra-chain.md) | Cosmos SDK | 1 | 33 (2 critical, 1 major) |
| [EMI wallet (architecture review)](protocols/emi-wallet.md) | Custody, settlement, brokerage | — | *Client under NDA; no public report* |
