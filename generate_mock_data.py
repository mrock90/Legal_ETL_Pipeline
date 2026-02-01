import pandas as pd
import random

def generate_mock_legal_data():
    # 1. Setup basic dimensions
    invoices = [f"INV-{i}" for i in range(1001, 1021)]
    clients = ["Global Tech Corp", "Blue Horizon LLC", "Stark Industries", "Wayne Ent", "Acme Co"]
    attorneys = ["M. Rockhold", "J. Doe", "A. Smith", "S. Johnson"]
    buckets = ["0-30", "31-60", "61-90", "91+"]

    # --- Generate OPEN INVOICES ---
    open_data = {
        " CLIENT NAME ": [random.choice(clients) for _ in invoices], # Note the intentional spaces
        "Matter Name": ["General Litigation" for _ in invoices],
        "Attorney Originating Matter": [random.choice(attorneys) for _ in invoices],
        "Attorney Working on Matter": [random.choice(attorneys) for _ in invoices],
        "Invoice Number": invoices,
        "Amount of Invoice Outstanding": [random.randint(5000, 50000) for _ in invoices],
        "Days Outstanding": [random.randint(1, 120) for _ in invoices],
        "Aged Bucket": [random.choice(buckets) for _ in invoices]
    }
    pd.DataFrame(open_data).to_csv("mock_open_invoices.csv", index=False)

    # --- Generate PAID RECORDS (Sub-section of invoices) ---
    paid_data = {
        "invoice_number": invoices[:10], # Only 10 are paid
        "amount_of_invoices_paid": [random.randint(5000, 20000) for _ in range(10)],
        "attorney_amount_earned": [random.randint(1000, 5000) for _ in range(10)],
        "split_%": [0.25 for _ in range(10)],
        "attorney_paid_date": ["2026-01-15" for _ in range(10)],
        "amount_ols_paid": [500 for _ in range(10)],
        "ols_paid_date": ["2026-01-20" for _ in range(10)]
    }
    pd.DataFrame(paid_data).to_csv("mock_paid_records.csv", index=False)

    # --- Generate COLLECTIONS ---
    coll_data = {
        "invoice_number": invoices[10:15], 
        "client_name": [random.choice(clients) for _ in range(5)],
        "amount_of_invoice_outstanding": [random.randint(10000, 30000) for _ in range(5)],
        "days_outstanding": [125, 130, 145, 160, 180], # Exactly 5 items
        "aged_bucket": ["91+", "91+", "91+", "91+", "91+"], # Exactly 5 items
        "status_update": ["Email Sent", "Follow-up Scheduled", "Promise to Pay", "Disputed", "Legal Review"], # Exactly 5 items
        "apr_notes": ["Client requested credit", "Waiting on check", "Address change", "Contacted AP", "Standard delay"] # Exactly 5 items
    }
    pd.DataFrame(coll_data).to_csv("mock_collections.csv", index=False)

    print("✨ Mock Law Firm data generated: mock_open_invoices.csv, mock_paid_records.csv, mock_collections.csv")

if __name__ == "__main__":
    generate_mock_legal_data()