CREATE TABLE expirationDate(
    id SERIAL PRIMARY KEY NOT NULL,
    itemName TEXT NOT NULL,
    SKU INT NOT NULL,
    amount INT NOT NULL DEFAULT 1
    dateExpired TIMESTAMP NOT NULL,
)


INSERT INTO expirationDate(itemName, SKU, amount, dateExpired) VALUES
    ('Test1', 1234567890, 21, '2020-01-01');
    