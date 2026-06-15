import sqlite3
import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), 'sales.db')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS categories (
            category_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS products (
            product_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            category_id  INTEGER,
            unit_price   REAL NOT NULL,
            stock        INTEGER DEFAULT 0,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        );

        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name   TEXT NOT NULL,
            email       TEXT,
            city        TEXT
        );

        CREATE TABLE IF NOT EXISTS orders (
            order_id    INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            order_date  TEXT NOT NULL,
            status      TEXT DEFAULT 'Completed',
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );

        CREATE TABLE IF NOT EXISTS order_items (
            item_id    INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id   INTEGER,
            product_id INTEGER,
            quantity   INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            FOREIGN KEY (order_id)   REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        );
    """)

    if cursor.execute("SELECT COUNT(*) FROM products").fetchone()[0] == 0:
        cursor.executescript("""
            INSERT INTO categories (category_name) VALUES
                ('Electronics'), ('Clothing'), ('Food & Beverages'), ('Books'), ('Sports');

            INSERT INTO products (product_name, category_id, unit_price, stock) VALUES
                ('Samsung Galaxy S24',    1, 3200.00, 50),
                ('iPhone 15',            1, 4500.00, 30),
                ('Sony Headphones WH1000',1,  950.00, 80),
                ('Nike Running Shoes',   5,  450.00,120),
                ('Adidas T-Shirt',       2,  120.00,200),
                ('Levi Jeans',           2,  280.00,150),
                ('Arabic Coffee Pack',   3,   85.00,500),
                ('Programming with Python',4, 195.00, 90),
                ('Clean Code Book',      4,  220.00, 75),
                ('Gym Gloves Pro',       5,   65.00,300);

            INSERT INTO customers (full_name, email, city) VALUES
                ('Ahmed Al-Rashid',  'ahmed@email.com',  'Riyadh'),
                ('Sara Al-Otaibi',   'sara@email.com',   'Jeddah'),
                ('Khalid Al-Zahrani','khalid@email.com', 'Dammam'),
                ('Fatima Al-Ghamdi', 'fatima@email.com', 'Riyadh'),
                ('Omar Al-Harbi',    'omar@email.com',   'Mecca'),
                ('Nora Al-Qahtani',  'nora@email.com',   'Jeddah'),
                ('Tariq Al-Shammari','tariq@email.com',  'Riyadh'),
                ('Mona Al-Dosari',   'mona@email.com',   'Dammam');

            INSERT INTO orders (customer_id, order_date, status) VALUES
                (1,'2024-01-05','Completed'),(2,'2024-01-12','Completed'),
                (3,'2024-02-03','Completed'),(4,'2024-02-18','Completed'),
                (5,'2024-03-07','Completed'),(1,'2024-03-22','Completed'),
                (6,'2024-04-10','Completed'),(7,'2024-04-25','Completed'),
                (2,'2024-05-08','Completed'),(8,'2024-05-19','Completed'),
                (3,'2024-06-02','Completed'),(4,'2024-06-15','Completed'),
                (5,'2024-07-01','Completed'),(6,'2024-07-20','Completed'),
                (1,'2024-08-05','Completed'),(7,'2024-08-18','Completed'),
                (2,'2024-09-10','Completed'),(8,'2024-09-25','Completed'),
                (3,'2024-10-08','Completed'),(4,'2024-10-22','Completed'),
                (5,'2024-11-05','Completed'),(6,'2024-11-19','Completed'),
                (7,'2024-12-03','Completed'),(8,'2024-12-20','Completed');

            INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
                (1,1,1,3200),(1,7,2,85),(2,2,1,4500),(2,5,3,120),
                (3,3,2,950),(3,8,1,195),(4,4,1,450),(4,6,2,280),
                (5,9,1,220),(5,10,4,65),(6,1,1,3200),(6,3,1,950),
                (7,2,1,4500),(7,5,2,120),(8,4,2,450),(8,7,3,85),
                (9,6,1,280),(9,8,2,195),(10,1,1,3200),(10,10,5,65),
                (11,2,1,4500),(11,9,1,220),(12,3,1,950),(12,5,4,120),
                (13,4,1,450),(13,7,2,85),(14,1,2,3200),(14,8,1,195),
                (15,2,1,4500),(15,6,3,280),(16,3,2,950),(16,10,6,65),
                (17,4,1,450),(17,9,2,220),(18,5,5,120),(18,7,4,85),
                (19,1,1,3200),(19,8,1,195),(20,2,1,4500),(20,3,1,950),
                (21,6,2,280),(21,4,2,450),(22,9,1,220),(22,10,3,65),
                (23,1,1,3200),(23,5,2,120),(24,2,1,4500),(24,7,5,85);
        """)

    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('dashboard.html')


@app.route('/api/total-sales')
def total_sales():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            COUNT(DISTINCT o.order_id)    AS total_orders,
            SUM(oi.quantity * oi.unit_price) AS total_revenue,
            COUNT(DISTINCT o.customer_id) AS total_customers
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.status = 'Completed'
    """)
    row = cursor.fetchone()
    conn.close()
    return jsonify(dict(row))


@app.route('/api/top-products')
def top_products():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            p.product_name,
            SUM(oi.quantity)                 AS units_sold,
            SUM(oi.quantity * oi.unit_price) AS revenue
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        JOIN orders o   ON oi.order_id   = o.order_id
        WHERE o.status = 'Completed'
        GROUP BY p.product_id, p.product_name
        ORDER BY revenue DESC
        LIMIT 5
    """)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return jsonify(rows)


@app.route('/api/monthly-revenue')
def monthly_revenue():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            strftime('%Y-%m', o.order_date)  AS month,
            SUM(oi.quantity * oi.unit_price) AS revenue
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.status = 'Completed'
        GROUP BY month
        ORDER BY month
    """)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return jsonify(rows)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
