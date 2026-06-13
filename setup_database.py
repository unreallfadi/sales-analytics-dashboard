"""
setup_database.py

Builds sales_analytics.db from the SQLite-compatible schema and seed
data files. Run this once before opening sales_analysis.ipynb or
running app.py.

Usage:
    python setup_database.py
"""

import os
import sqlite3

DB_FILE = "sales_analytics.db"
SCHEMA_FILE = "sales_schema_sqlite.sql"
DATA_FILE = "sales_data_sqlite.sql"


def build_database() -> None:
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    with open(SCHEMA_FILE) as f:
        cursor.executescript(f.read())

    with open(DATA_FILE) as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print(f"{DB_FILE} created successfully.")


if __name__ == "__main__":
    build_database()
