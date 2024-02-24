CREATE TABLE IF NOT EXISTS products (
    prod_id INT PRIMARY KEY AUTO_INCREMENT,
    prod_name VARCHAR(20),
    price DECIMAL(10,2),
    quantity INT
);

INSERT INTO products (prod_id, prod_name, price, quantity)
VALUES (%s, '%s', %s, %s);

UPDATE products
SET prod_name = '%s', price = %s, quantity = %s
WHERE prod_id = %s;

DELETE FROM products WHERE prod_id = %s;