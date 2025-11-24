# sales_summary.py
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "sales_data.db"
CHART_PATH = "sales_chart.png"

def query_summary(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    query = """
    SELECT
        product,
        SUM(quantity) AS total_qty,
        SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def save_chart(df, out=CHART_PATH):
    ax = df.plot(kind='bar', x='product', y='revenue', legend=False)
    ax.set_xlabel("Product")
    ax.set_ylabel("Revenue")
    ax.set_title("Revenue by Product")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"Saved chart to {out}")

def main():
    df = query_summary()
    if df.empty:
        print("No data returned. Make sure sales_data.db exists and has rows.")
        return

    print("\nSales summary by product:\n")
    print(df.to_string(index=False, float_format='{:,.2f}'.format))
    save_chart(df)

if __name__ == "__main__":
    main()
