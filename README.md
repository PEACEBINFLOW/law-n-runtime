# LAW-N RUNTIME (LNRE)

**SAGEWORKS AI — Mind’s Eye Cognition Division**

The **LAW-N Runtime Environment (LNRE)** is the execution core for the
LAW-N Network-Time Programming Model. It interprets LAW-N instructions,
executes N-SQL operations, and manages time-aware state transitions.

LNRE is designed for:

- Deterministic, time-aware execution of LAW-N programs
- N-SQL evaluation with temporal semantics
- Signal + channel routing between logical nodes
- Introspection of binary timing and state transitions

---

## ✨ Key Concepts

- **LAW-N** — network + time native programming model
- **N-SQL** — Network-SQL: SQL extended with time, channel, and flow semantics
- **LNRE** — LAW-N Runtime Environment: the VM + execution engine

---

## 📂 Project Layout

See [`docs/runtime-overview.md`](docs/runtime-overview.md) for the architecture.

- `lnre/` — runtime source (VM, bytecode, parser, router, N-SQL executor)
- `examples/` — sample LAW-N programs
- `tests/` — unit tests
- `docs/` — internal documentation and specs

---

## 🚀 Quickstart

```bash
git clone https://github.com/PEACEBINFLOW/law-n-runtime
cd law-n-runtime
pip install -e .
