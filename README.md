📘 Task 7 — Sales Summary (SQLite + Python)

This project creates a simple SQLite sales database, runs SQL queries using Python, summarizes the results with pandas, and generates a bar chart using matplotlib.

It follows the instructions from the uploaded task file
➡️ task_7_spec.pdf

📂 Project Structure
task7-sales-summary/
│
├── create_sales_db.py       # Creates sample sales database
├── sales_summary.py         # Runs SQL + summary + chart
├── sales_data.db            # Generated SQLite database
├── sales_chart.png          # Generated bar chart
├── venv/                    # Virtual environment
├── task_7_spec.pdf          # Uploaded task instructions
└── README.md                # Documentation

⚙️ Requirements

Python 3.8+

pandas

matplotlib

sqlite3 (built into Python)

🚀 How to Run (VS Code)
1. Create and activate virtual environment

Windows PowerShell:

python -m venv venv
.\venv\Scripts\Activate.ps1

2. Install dependencies
pip install pandas matplotlib

3. Create the SQLite database
python create_sales_db.py


This generates:

sales_data.db

4. Run the summary script
python sales_summary.py


This will:

Print total quantity + revenue per product

Create a bar chart file: sales_chart.png

📊 Output Example
Terminal summary example:
Product     Total Qty     Revenue
Widget A       20         199.80
Widget B        8         159.92
Widget C       17          76.50
Widget D        4         119.96

Generated Chart:

✔ Saved as: sales_chart.png

🧠 What This Project Demonstrates

Creating and inserting data into an SQLite database

Running SQL queries from Python

Using pandas.read_sql_query()

Generating bar charts with matplotlib

Working with VS Code virtual environments

📎 Task File

The original task instructions are included:

task_7_spec.pdf

