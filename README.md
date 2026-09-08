<div align="center">

# ⚡ my_dev_crew

**Collaborative Multi-Agent Intelligence Framework**

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/CrewAI-Agentic%20Flow-FF4B4B?style=for-the-badge)](https://crewai.com)
[![Package Manager: uv](https://img.shields.io/badge/managed%20by-uv-DE5FE9?style=for-the-badge)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)

<p align="center">
  An autonomous, multi-agent orchestration pipeline built on CrewAI. Distributes complex development workflows across specialized agents featuring declarative configuration, persistent context, and modular tools.
</p>

---

</div>

## 📌 Architecture Overview

This project executes synchronized agentic workflows using role-playing autonomous agents:

* **Autonomous Execution:** Agents synthesize context, invoke tools, delegate subtasks, and refine outputs dynamically.
* **Declarative Configuration:** Agent personas, objectives, and task parameters are defined via YAML files in `config/`.
* **Domain Knowledge Integration:** Incorporates local contextual embeddings and reference files housed in `knowledge/`.
* **Testing & Verification:** Automated test suites located in `tests/` ensure stable orchestration across runs.

---

## 📂 Repository Structure

```text
my_dev_crew/
├── config/
│   ├── agents.yaml       # Agent roles, goals, and backstories
│   └── tasks.yaml        # Task definitions and deliverables
├── knowledge/            # Local data sources, documents, and reference context
├── src/                  # Core source modules and custom agent tools
├── tests/                # Unit and integration test suites
├── crew.py               # Crew orchestration, processes, and memory
├── main.py               # CLI entry point, inputs, and kickoff commands
├── pyproject.toml        # Project dependencies and packaging configuration
├── uv.lock               # Deterministic dependency lockfile
├── .env.example          # Environment variable template
├── .gitignore            # Git exclusion rules
└── README.md             # Project documentation
