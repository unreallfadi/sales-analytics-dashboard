INSERT INTO categories (category_name) VALUES
('Electronics'), ('Clothing'), ('Food & Beverages'), ('Books'), ('Sports');

INSERT INTO products (product_name, category_id, unit_price, stock) VALUES
('Samsung Galaxy S24', 1, 3200.00, 50),
('iPhone 15', 1, 4500.00, 30),
('Sony Headphones WH1000', 1, 950.00, 80),
('Nike Running Shoes', 5, 450.00, 120),
('Adidas T-Shirt', 2, 120.00, 200),
('Levi Jeans', 2, 280.00, 150),
('Arabic Coffee Pack', 3, 85.00, 500),
('Programming with Python', 4, 195.00, 90),
('Clean Code Book', 4, 220.00, 75),
('Gym Gloves Pro', 5, 65.00, 300);

INSERT INTO customers (full_name, email, city) VALUES
('Ahmed Al-Rashid', 'ahmed@email.com', 'Riyadh'),
('Sara Al-Otaibi', 'sara@email.com', 'Jeddah'),
('Khalid Al-Zahrani', 'khalid@email.com', 'Dammam'),
('Fatima Al-Ghamdi', 'fatima@email.com', 'Riyadh'),
('Omar Al-Harbi', 'omar@email.com', 'Mecca'),
('Nora Al-Qahtani', 'nora@email.com', 'Jeddah'),
('Tariq Al-Shammari', 'tariq@email.com', 'Riyadh'),
('Mona Al-Dosari', 'mona@email.com', 'Dammam');

INSERT INTO orders (customer_id, order_date, status) VALUES
(1, '2024-01-05', 'Completed'), (2, '2024-01-12', 'Completed'),
(3, '2024-02-03', 'Completed'), (4, '2024-02-18', 'Completed'),
(5, '2024-03-07', 'Completed'), (1, '2024-03-22', 'Completed'),
(6, '2024-04-10', 'Completed'), (7, '2024-04-25', 'Completed'),
(2, '2024-05-08', 'Completed'), (8, '2024-05-19', 'Completed'),
(3, '2024-06-02', 'Completed'), (4, '2024-06-15', 'Completed'),
(5, '2024-07-01', 'Completed'), (6, '2024-07-20', 'Completed'),
(1, '2024-08-05', 'Completed'), (7, '2024-08-18', 'Completed'),
(2, '2024-09-10', 'Completed'), (8, '2024-09-25', 'Completed'),
(3, '2024-10-08', 'Completed'), (4, '2024-10-22', 'Completed'),
(5, '2024-11-05', 'Completed'), (6, '2024-11-19', 'Completed'),
(7, '2024-12-03', 'Completed'), (8, '2024-12-20', 'Completed');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 1, 3200.00), (1, 7, 2, 85.00),
(2, 2, 1, 4500.00), (2, 5, 3, 120.00),
(3, 3, 2, 950.00), (3, 8, 1, 195.00),
(4, 4, 1, 450.00), (4, 6, 2, 280.00),
(5, 9, 1, 220.00), (5, 10, 4, 65.00),
(6, 1, 1, 3200.00), (6, 3, 1, 950.00),
(7, 2, 1, 4500.00), (7, 5, 2, 120.00),
(8, 4, 2, 450.00), (8, 7, 3, 85.00),
(9, 6, 1, 280.00), (9, 8, 2, 195.00),
(10, 1, 1, 3200.00), (10, 10, 5, 65.00),
(11, 2, 1, 4500.00), (11, 9, 1, 220.00),
(12, 3, 1, 950.00), (12, 5, 4, 120.00),
(13, 4, 1, 450.00), (13, 7, 2, 85.00),
(14, 1, 2, 3200.00), (14, 8, 1, 195.00),
(15, 2, 1, 4500.00), (15, 6, 3, 280.00),
(16, 3, 2, 950.00), (16, 10, 6, 65.00),
(17, 4, 1, 450.00), (17, 9, 2, 220.00),
(18, 5, 5, 120.00), (18, 7, 4, 85.00),
(19, 1, 1, 3200.00), (19, 8, 1, 195.00),
(20, 2, 1, 4500.00), (20, 3, 1, 950.00),
(21, 6, 2, 280.00), (21, 4, 2, 450.00),
(22, 9, 1, 220.00), (22, 10, 3, 65.00),
(23, 1, 1, 3200.00), (23, 5, 2, 120.00),
(24, 2, 1, 4500.00), (24, 7, 5, 85.00);
