<h3 align="center">🛠️ read-sync</h3>

<div align="center">
  <a href="https://github.com/yourorg/read-sync/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python 3.10+"></a>
  <a href="https://github.com/yourorg/read-sync/actions"><img src="https://img.shields.io/github/actions/workflow/status/yourorg/read-sync/ci.yml?branch=main&label=build" alt="Build Status"></a>
  <a href="https://github.com/yourorg/read-sync"><img src="https://img.shields.io/github/stars/yourorg/read-sync.svg?style=social" alt="GitHub stars"></a>
</div>

---

# 🚀 read-sync  
**Power developers with seamless reading‑position synchronization.**  
A lightweight service that lets you **save**, **retrieve**, **push**, and **pull** reading positions across any device—no third‑party servers, no ads, full data ownership.

## Why read-sync?  

- **Zero‑Server Dependency** – All data stays on‑premise, giving users complete control.  
- **Cross‑Platform** – Works with major e‑reader formats (ePub, PDF, MOBI) and any device that can call the API.  
- **Conflict‑Free Sync** – Built‑in conflict‑resolution guarantees the latest position wins.  
- **Developer‑First API** – Simple Pythonic interface, perfect for integration into existing reading apps.  
- **Ad‑Free Experience** – No trackers, no telemetry; just pure synchronization.  
- **Self‑Hosted** – Deploy anywhere—local machine, Docker, or your own cloud.  
- **Early‑Stage, Actively Evolving** – Frequent updates based on community feedback.

## Feature Overview  

| Feature | Description |
|---------|-------------|
| **Save Position** | Persist a user's current location (chapter, offset, timestamp). |
| **Get Position** | Retrieve the latest saved location for a given user/book. |
| **Push / Pull** | Push local changes to the server and pull remote updates in one call. |
| **Conflict Resolution** | Automatic “last‑write‑wins” algorithm with optional custom hooks. |
| **Multi‑Format Support** | Works with ePub, PDF, MOBI, and any custom format via adapters. |
| **Stateless Service** | No session storage; all state is encoded in the payloads. |
| **Extensible Hooks** | Plug‑in hooks for logging, analytics, or custom merge strategies. |

## Tech Stack  

- **Python** – Core language, type‑hinted for safety.  
- **Poetry** – Dependency management & packaging.  

*(Matches the locked tech‑stack decisions.)*

## Project Structure  

```
read-sync/
├─ business/      # Business‑logic layer (service orchestration)
├─ docs/          # Documentation assets (PRD, ROADMAP, etc.)
├─ src/           # Core library implementation
├─ tests/         # Unit & integration test suite
├─ pyproject.toml # Poetry configuration & entry points
├─ requirements.txt # Pin‑file for CI environments
└─ README.md      # ← you are here
```

## Getting Started  

```bash
# 1️⃣ Clone the repo
git clone https://github.com/yourorg/read-sync.git
cd read-sync

# 2️⃣ Install dependencies via Poetry
poetry install

# 3️⃣ Run the service (exposes a local HTTP API on 8000)
poetry run python -m read_sync

# 4️⃣ Run the test suite
poetry run pytest
```

## Deploy  

The service can be run directly with Python or containerised with Docker.

**Run locally (Python):**

```bash
poetry run python -m read_sync --host 0.0.0.0 --port 8000
```

**Run with Docker (example Dockerfile in `docs/`):**

```bash
docker build -t read-sync:latest .
docker run -p 8000:8000 read-sync:latest
```

*(Adjust the Dockerfile to your environment; the stack remains pure Python/Poetry.)*

## Status  

Early‑stage, actively maintained. Recent commits showcase a sandbox‑tested implementation and documentation polish:

- `12b6f36` – DR snapshot (2026‑06‑28)  
- `449d532` – Docs cycle decision (2026‑06‑25)  
- `39ff2ab` – Real implementation, sandbox‑tested (2026‑06‑24)  

## Contributing  

We welcome contributions! Please read our [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to propose changes, run tests, and submit pull requests.

## License  

This project is licensed under the **MIT License**.