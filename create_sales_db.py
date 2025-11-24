# create_sales_db.py
import sqlite3

def create_db(path="sales_data.db"):
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    # Create table (safe to rerun)
    cur.execute("DROP TABLE IF EXISTS sales;")
    cur.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        product TEXT,
        quantity INTEGER,
        price REAL
    );
    """)

    # Sample data (edit these rows if you want real data)
    rows = [
        ("2025-11-01", "Widget A", 10, 9.99),
        ("2025-11-01", "Widget B", 5, 19.99),
        ("2025-11-02", "Widget A", 2, 9.99),
        ("2025-11-02", "Widget C", 7, 4.50),
        ("2025-11-03", "Widget B", 3, 19.99),
        ("2025-11-03", "Widget C", 10, 4.50),
        ("2025-11-04", "Widget A", 8, 9.99),
        ("2025-11-04", "Widget D", 4, 29.99),
    ]

    cur.executemany(
        "INSERT INTO sales (date, product, quantity, price) VALUES (?, ?, ?, ?);",
        rows
    )

    conn.commit()
    conn.close()
    print(f"Created {path} with sample data.")

if __name__ == "__main__":
    create_db()
