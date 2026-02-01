import pandas as pd
import sqlite3
import os
import glob

def clean_and_slice(df, table_name):
    # Standardize headers: lowercase, remove spaces, remove special characters
    df.columns = [c.replace(' ', '_').lower().strip() for c in df.columns]

    # --- The Surgical Slice ---

    if 'open' in table_name:
        cols = ['client_name', 'matter_name', 'attorney_originating_matter', 'attorney_working_on_matter', 'invoice_number', 'amount_of_invoice_outstanding', 'days_outstanding', 'aged_bucket']
    
    elif 'paid' in table_name:
        cols = ['invoice_number', 'amount_of_invoices_paid', 'attorney_amount_earned', 'split_%', 'attorney_paid_date', 'amount_ols_paid', 'ols_paid_date']

    elif 'attorney' in table_name:
        cols = ['first_name', 'last_name', 'omnus_email', 'book_of_business_(currency)', 'primary_practice_state_(drop_down)']

    elif 'iolta' in table_name:
        cols = ['client_name', 'funds_flow', 'amount_of_transaction', 'invoice_number']

    elif 'collection' in table_name:
        cols = ['invoice_number', 'client_name', 'amount_of_invoice_outstanding', 'days_outstanding', 'aged_bucket', 'status_update', 'apr_notes'] 

    else:
        return df.fillna(0)
    
    # Filter to keep the columns that exist in the file
    existing_cols = [c for c in cols if c in df.columns]

    if not existing_cols:
        print(f'⚠️ Warning: No matching columns found for {table_name}. Check headers!')
        return df.fillna(0)
    
    return df[existing_cols].fillna(0)

def run_ingestion_pipeline():
    conn= sqlite3.connect('finance_sandbox.db')

    # Search for .csv files
    csv_files = glob.glob('*.csv')

    for file in csv_files:
        name_clean = os.path.basename(file).lower()

        # Table name logic
        if 'open' in name_clean: table_name = 'stg_open'
        elif 'paid' in name_clean: table_name = 'stg_paid'
        elif 'iolta' in name_clean: table_name = 'stg_iolta'
        elif 'attorney' in name_clean: table_name = 'stg_attorneys'
        elif 'collection' in name_clean: table_name = 'stg_collections'
        else: continue

        print(f'Processing: {file} -> {table_name}')

        try:
            # Read CSV files
            df_raw = pd.read_csv(file)
            df_final = clean_and_slice(df_raw, table_name)
            df_final.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f'✅ Successfully ingested {len(df_final)} rows.')

        except Exception as e:
            print(f'❌ Error processing {file}: {e}')

    conn.close()
    print('\n--- Pipeline Complete: SQL Sandbox Updated ---')


if __name__ =='__main__':
    # Test it by running this file directly
    # Make sure is in the same folder
    run_ingestion_pipeline()