# Legal Revenue ETL Pipeline

### Project Overview
A modular Python-based ETL (Extract, Transform, Load) framework designed to architect a "Single Source of Truth" from disparate legal ERP data streams. This system automates the ingestion, normalization, and validation of high-stakes financial data, bridging the gap between legacy system exports and modern analytics environments.

### Core Engineering Features
* **Data Normalization & Schema Integrity: Implements a robust mapping layer to standardize inconsistent headers and enforce strict data typing across Open, Paid, IOLTA, and Collections datasets.
* **Automated Validation Logic: Features backend logic to resolve legacy encoding conflicts and deduplicate entries, ensuring 100% data fidelity—a critical prerequisite for AI-driven financial modeling.
* **Dynamic SQL Orchestration: Automatically constructs and updates a SQLite "Analytics Sandbox," enabling complex relational queries and real-time revenue trend analysis.
* **Event-Driven Architecture: Utilizes a "Watchdog" service logic to monitor system directories and trigger automated ingestion upon file detection, removing manual friction from the reporting lifecycle.

###Technical Stack
* **Language: Python 3.x
* **Libraries: Pandas (Data Orchestration), SQLite3 (Persistence Layer), OS/Glob (File System Automation)
* **Environment: VS Code / Git

### How to Run
1. Run `python generate_mock_data.py` to create synthetic legal records.
2. Run `python pipeline_logic.py` to ingest records into `finance_sandbox.db`.
