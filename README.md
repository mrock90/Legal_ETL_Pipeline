# Legal Revenue ETL Pipeline

### Project Overview
A Python-based ETL pipeline designed to automate the ingestion and standardization of law firm revenue data. This project simulates a "Watchdog" style service that takes raw exports from legal ERP systems (like Aderant or Filevine) and prepares them for SQL-based financial analysis.

### Features
* **Schema Enforcement:** Standardizes "dirty" headers and enforces data types.
* **Revenue Lifecycle Mapping:** Handles Open Invoices, Paid Records, IOLTA, and Collections.
* **SQL Sandbox:** Automatically builds and updates a SQLite database for real-time reporting.

### How to Run
1. Run `python generate_mock_data.py` to create synthetic legal records.
2. Run `python pipeline_logic.py` to ingest records into `finance_sandbox.db`.