import sqlite3
import pandas as pd
import os

# Input CSV
CSV_PATH = "/data2/2_Suvrajit_Mullick/Pushpendra_Jaiswal/Stock_Data_Agent/data/apple_stock_data.csv"

# Output DB
DB_PATH = "db/stock.db"

def build_sqlite_db():
    print("📊 Loading CSV...")
    df = pd.read_csv(CSV_PATH)

    print("Preview data:")
    print(df.head())

    # Create DB folder if not exists
    os.makedirs("db", exist_ok=True)

    print("🗄️ Creating SQLite DB...")
    conn = sqlite3.connect(DB_PATH)

    # Store table
    df.to_sql("stocks", conn, if_exists="replace", index=False)

    conn.close()

    print(f"✅ SQLite DB created at {DB_PATH}")
    print("Table name: stocks")


if __name__ == "__main__":
    build_sqlite_db()