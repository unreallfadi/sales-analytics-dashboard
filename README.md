# Sales Analytics Dashboard

A web-based sales analytics dashboard built with Flask, SQLite, and Chart.js.
It displays real-time KPIs, top product performance, and order data through an interactive interface.

---

## Features

- KPI cards showing total revenue, total orders, and total customers
- Bar chart for top 5 products by revenue
- Doughnut chart for units sold distribution
- Product breakdown table with visual progress bars
- Data served through a REST API built with Flask

---

## Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Backend    | Python, Flask     |
| Database   | SQLite            |
| Frontend   | HTML5, CSS3, JavaScript |
| Charts     | Chart.js          |

---

## Database Schema

The database consists of 5 tables:

- **categories** - product categories
- **products** - product details linked to categories
- **customers** - customer information
- **orders** - order records linked to customers
- **order_items** - individual items within each order (links orders to products)

The database is created and seeded automatically on first run.

---

## Project Structure

```
sales-analytics-dashboard/
|-- app.py               # Flask application and API routes
|-- dashboard.html       # Frontend dashboard
|-- sales_schema.sql     # Database schema reference
|-- sales_data.sql       # Sample data reference
|-- README.md
```

---

## Getting Started

### Requirements

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/unreallfadi/sales-analytics-dashboard.git
cd sales-analytics-dashboard
```

2. Install dependencies:

```bash
pip install flask
```

3. Run the application:

```bash
python app.py
```

4. Open your browser and go to:

```
http://127.0.0.1:5000
```

The database will be created and populated with sample data automatically on first run.

---

## API Endpoints

| Endpoint            | Method | Description                          |
|---------------------|--------|--------------------------------------|
| `/`                 | GET    | Serves the dashboard page            |
| `/api/total-sales`  | GET    | Returns total revenue, orders, and customers |
| `/api/top-products` | GET    | Returns top 5 products by revenue    |

---

## Author

Fadi - IT Student, Semester 4  
GitHub: [unreallfadi](https://github.com/unreallfadi)
