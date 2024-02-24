CREATE TABLE IF NOT EXISTS transactions (
    t_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    prod_name VARCHAR(20),
    price DECIMAL(10,2),
    datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_quantity INT,
    FOREIGN KEY (product_id) REFERENCES products(prod_id) ON DELETE CASCADE
);

INSERT INTO transactions (product_id, prod_name, price, updated_quantity)
VALUES (%s, '%s', %s, %s);

DELETE FROM transactions WHERE t_id = %s;