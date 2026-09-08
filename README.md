<div align="center">

# ⚡ my_crewai_project

**Collaborative Multi-Agent Intelligence Framework**

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/CrewAI-Agentic%20Flow-FF4B4B?style=for-the-badge)](https://crewai.com)
[![Editor](https://img.shields.io/badge/Built%20With-Cursor%20AI-000000?style=for-the-badge&logo=cursor&logoColor=white)](https://www.cursor.com/)
[![Package Manager: uv](https://img.shields.io/badge/managed%20by-uv-DE5FE9?style=for-the-badge)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)

<p align="center">
  An autonomous, multi-agent orchestration pipeline built with CrewAI and developed using Cursor AI. Distributes complex development workflows across specialized agents featuring declarative configuration, persistent context, and modular tools.
</p>

---

</div>

## 📌 Architecture Overview

This project executes synchronized agentic workflows using role-playing autonomous agents:

* **Autonomous Execution:** Agents synthesize context, invoke tools, delegate subtasks, and refine outputs dynamically.
* **Declarative Configuration:** Agent personas, objectives, and execution parameters are managed cleanly through YAML files in `src/my_dev_crew/config/`.
* **Fast Dependency Management:** Managed with `uv` for rapid virtual environment setup and deterministic lockfiles.

---

## 🧠 Skills Learned & Core Competencies

* **Agentic Systems Architecture:** Designed role-playing multi-agent systems using CrewAI, implementing sequential workflows, task delegation, and context handoffs.
* **Declarative System Design:** Structured complex prompts, agent objectives, and deliverable schemas decoupled from application logic via YAML.
* **AI-Augmented Engineering (Cursor AI):** Leveraged Cursor's agentic coding, context indexing, inline model directives, and prompt engineering to scaffold, refactor, and debug multi-file Python architectures.
* **Modern Python Packaging & Tooling:** Configured PEP 621-compliant project specifications (`pyproject.toml`) and deterministic dependency management via `uv`.
* **API Integration & Security:** Orchestrated LLM provider integrations while adhering to strict environment variable security practices.

---

## 📂 Repository Structure

```text
my_dev_crew/
├── src/
│   └── my_dev_crew/
│       └── config/
│           ├── agents.yaml      # Agent roles, goals, and backstories
│           └── tasks.yaml       # Task definitions and deliverables
├── crew.py                      # Crew orchestration, processes, and memory
├── main.py                      # CLI entry point, inputs, and kickoff commands
├── pyproject.toml               # Project dependencies and packaging configuration
├── uv.lock                      # Deterministic dependency lockfile
├── .env.example                 # Environment variable template
├── .gitignore                   # Git exclusion rules
├── LICENSE                      # MIT License terms
└── README.md                    # Project documentation
