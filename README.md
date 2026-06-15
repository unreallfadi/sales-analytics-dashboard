# Sales Analytics Dashboard

An interactive sales analytics dashboard built with Flask, SQLite, and Chart.js.
Designed to demonstrate end-to-end data pipeline skills: schema design, data ingestion, API layer, and visual reporting.

---

## Features

- KPI cards: Total Revenue, Orders, Customers
- Bar chart: Top 5 products by revenue
- Doughnut chart: Units sold distribution
- Product breakdown table with progress bars
- REST API endpoints for chart data

---

## Tech Stack

| Layer     | Technology          |
|-----------|---------------------|
| Backend   | Python 3, Flask     |
| Database  | SQLite              |
| Frontend  | HTML5, CSS3, JS     |
| Charts    | Chart.js            |

---

## Project Structure
sales-analytics-dashboard/

├── app.py              # Flask app, DB init, API routes

├── dashboard.html      # Frontend dashboard

├── sales_schema.sql    # Reference schema (MySQL-compatible)

├── sales_data.sql      # Reference seed data

├── requirements.txt    # Python dependencies

├── .gitignore

└── README.md

---

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/unreallfadi/sales-analytics-dashboard.git
cd sales-analytics-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Open: http://localhost:5000

The database is created automatically on first run.

---

## API Endpoints

| Endpoint           | Description                        |
|--------------------|------------------------------------|
| `GET /`            | Serves the dashboard UI            |
| `GET /api/total-sales`  | Returns total revenue, orders, customers |
| `GET /api/top-products` | Returns top 5 products by revenue        |

---

## Skills Demonstrated

- Relational schema design and normalization
- SQLite integration with Flask
- REST API design with JSON responses
- Data aggregation with SQL (SUM, COUNT, GROUP BY, JOIN)
- Frontend data visualization with Chart.js

---

**Fadi Amir**
Data Analyst | SQL Developer | Database Design

[![GitHub](https://img.shields.io/badge/GitHub-unreallfadi-181717?style=flat&logo=github)](https://github.com/unreallfadi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-fadi--amir-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/unreallfadi)
