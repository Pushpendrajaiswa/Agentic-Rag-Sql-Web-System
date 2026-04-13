import sqlite3

DB_PATH = "db/stock.db"

def clean_sql(query):
    query = query.strip()

    # Remove markdown formatting
    query = query.replace("```sql", "")
    query = query.replace("```", "")

    return query.strip()


def run_sql(query):
    try:
        query = clean_sql(query)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        print("Executing SQL:", query)

        cursor.execute(query)
        result = cursor.fetchall()

        conn.close()

        return result

    except Exception as e:
        return f"SQL Error: {str(e)}"