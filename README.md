# Sales Analytics Dashboard

A web-based sales analytics dashboard built with Flask, SQLite, and Chart.js, with a Python/Pandas data analysis layer on top.
It displays real-time KPIs, top product performance, and order data through an interactive interface, and includes a Jupyter notebook for deeper analysis and visualization.

---

## Features

- KPI cards showing total revenue, total orders, and total customers
- Bar chart for top 5 products by revenue
- Doughnut chart for units sold distribution
- Product breakdown table with visual progress bars
- Data served through a REST API built with Flask
- Jupyter notebook for data cleaning, trend analysis, and visualization (Pandas, Matplotlib, Seaborn)

---

## Tech Stack

| Layer            | Technology                        |
| ---------------- | ---------------------------------- |
| Backend          | Python, Flask                      |
| Database         | SQLite                              |
| Frontend         | HTML5, CSS3, JavaScript            |
| Charts (web)     | Chart.js                            |
| Data Analysis    | Pandas, Matplotlib, Seaborn, Jupyter |

---

## Database Schema

The database consists of 5 tables:

- **categories** - product categories
- **products** - product details linked to categories
- **customers** - customer information
- **orders** - order records linked to customers
- **order_items** - individual items within each order (links orders to products)

`sales_schema_sqlite.sql` and `sales_data_sqlite.sql` contain the SQLite-compatible schema and seed data used by `setup_database.py` and the analysis notebook.

---

## Project Structure

```
sales-analytics-dashboard/
|-- app.py                    # Flask application and API routes
|-- dashboard.html             # Frontend dashboard
|-- sales_schema.sql            # Database schema reference
|-- sales_data.sql              # Sample data reference
|-- sales_schema_sqlite.sql     # SQLite-compatible schema
|-- sales_data_sqlite.sql       # SQLite-compatible seed data
|-- setup_database.py           # Builds sales_analytics.db
|-- sales_analysis.ipynb        # Data analysis notebook
|-- README.md
```

---

## Getting Started

### Requirements

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:

```
git clone https://github.com/unreallfadi/sales-analytics-dashboard.git
cd sales-analytics-dashboard
```

2. Install dependencies:

```
pip install flask pandas matplotlib seaborn jupyter
```

3. Run the application:

```
python app.py
```

4. Open your browser and go to:

```
http://127.0.0.1:5000
```

The database will be created and populated with sample data automatically on first run.

### Running the Analysis Notebook

1. Build the analysis database:

```
python setup_database.py
```

2. Open `sales_analysis.ipynb` in Jupyter and run all cells.

---

## API Endpoints

| Endpoint            | Method | Description                                  |
| ------------------- | ------ | --------------------------------------------- |
| `/`                 | GET    | Serves the dashboard page                     |
| `/api/total-sales`  | GET    | Returns total revenue, orders, and customers  |
| `/api/top-products` | GET    | Returns top 5 products by revenue             |

---

## Data Analysis Notebook

`sales_analysis.ipynb` adds a Python analysis layer on top of the dashboard:

- Loads data from `sales_analytics.db` into Pandas
- Validates data quality (missing values, duplicates, data types)
- Builds a combined sales fact table joining orders, products, categories, and customers
- Visualizes revenue by category, monthly revenue trend, top products, and revenue by city
- Summarizes key findings (e.g. revenue concentration by product and region)

---

## Author

**Fadi** Data Analyst | SQL Developer | Database Design

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com) [![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com)
