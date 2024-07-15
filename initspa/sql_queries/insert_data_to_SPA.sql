-- Insert data to Stores Table 

INSERT INTO stores(
	store_name,
	location,
	contact_info
	)
VALUES
	('Apple Online Store', '{"type": "online", "address": "www.apple.com"}', '{"telephone": "+18006927753", "email": "contact@apple.com"}'),
	('Berlin Apple Store', '{"type": "offline", "address": "Kurfürstendamm 26, 10719 Berlin"}', '{"telephone": "+493020302000", "email": "berlin@apple.com"}'),
	('Samsung Online Store', '{"type": "online", "address": "www.samsung.com"}', '{"telephone": "+18001234567", "email": "contact@samsung.com"}'),
    ('Berlin Samsung Store', '{"type": "offline", "address": "Tauentzienstraße 9-12, 10789 Berlin"}', '{"telephone": "+493025760", "email": "berlin@samsung.com"}'),
    ('Microsoft Online Store', '{"type": "online", "address": "www.microsoft.com"}', '{"telephone": "+18005551234", "email": "contact@microsoft.com"}'),
    ('Berlin Microsoft Store', '{"type": "offline", "address": "Unter den Linden 17, 10117 Berlin"}', '{"telephone": "+493015991700", "email": "berlin@microsoft.com"}'),
    ('Sony Online Store', '{"type": "online", "address": "www.sony.com"}', '{"telephone": "+18004567890", "email": "contact@sony.com"}'),
    ('Hamburg Sony Store', '{"type": "offline", "address": "Mönckebergstraße 2, 20095 Hamburg"}', '{"telephone": "+494030987654", "email": "hamburg@sony.com"}'),
    ('Dell Online Store', '{"type": "online", "address": "www.dell.com"}', '{"telephone": "+18003344556", "email": "contact@dell.com"}'),
    ('Munich Dell Store', '{"type": "offline", "address": "Leopoldstraße 10, 80802 München"}', '{"telephone": "+498920304050", "email": "munich@dell.com"}');


-- Insert data to Categories Table 

INSERT INTO categories(
	category_name
	)
VALUES
	('Laptop'),
	('Smartphone'),
    ('Tablet'),
    ('PC'),
    ('Speakers W'),
    ('Speakers WL'),
    ('Headphones W'),
    ('Headphones WL'),
    ('Earbuds'),
    ('AR Glasses');


-- Insert data to Products Table

INSERT INTO products(
	product_name,
	category_id,
	details
	)
VALUES
	('MacBook Air', 1, '{"brand": "Apple", "specs": {"CPU": "Apple M1", "GPU": "Apple M1", "ram": "16GB", "storage": "256GB SSD"}}'),
	('iPhone 13', 2, '{"brand": "Apple", "specs": {"CPU": "A15 Bionic", "GPU": "A15 Bionic", "ram": "4GB", "storage": "128GB"}}'),
    ('Galaxy S21', 2, '{"brand": "Samsung", "specs": {"CPU": "Exynos 2100", "GPU": "Mali-G78", "ram": "8GB", "storage": "256GB"}}'),
    ('Surface Pro 7', 3, '{"brand": "Microsoft", "specs": {"CPU": "Intel i5", "GPU": "Intel Iris Plus", "ram": "8GB", "storage": "128GB SSD"}}'),
    ('XPS 13', 1, '{"brand": "Dell", "specs": {"CPU": "Intel i7", "GPU": "Intel Iris Xe", "ram": "16GB", "storage": "512GB SSD"}}'),
    ('PlayStation 5', 4, '{"brand": "Sony", "specs": {"CPU": "x86-64-AMD Ryzen Zen 8", "GPU": "AMD Radeon RDNA 2", "ram": "16GB", "storage": "825GB SSD"}}'),
    ('Sony WH-1000XM4', 7, '{"brand": "Sony", "specs": {"type": "Over-Ear", "battery": "30 hours", "noise_canceling": "Yes"}}'),
    ('Apple AirPods Pro', 9, '{"brand": "Apple", "specs": {"battery": "5 hours", "noise_canceling": "Yes", "wireless": "Yes"}}'),
    ('Samsung Galaxy Buds Pro', 9, '{"brand": "Samsung", "specs": {"battery": "8 hours", "noise_canceling": "Yes", "wireless": "Yes"}}'),
    ('Microsoft HoloLens 2', 10, '{"brand": "Microsoft", "specs": {"field_of_view": "52 degrees", "resolution": "2048x1080", "tracking": "inside-out"}}');


-- Insert data to Prices Table

INSERT INTO prices(
	product_id,
	store_id,
	currency,
	price
	)
VALUES
 	(1, 1, 'EUR', 1099.99),
    (2, 2, 'EUR', 899.99),
    (3, 3, 'EUR', 1099.99),
    (4, 4, 'EUR', 849.99),
    (5, 5, 'EUR', 1349.99),
    (6, 6, 'EUR', 549.99),
    (7, 7, 'EUR', 399.99),
    (8, 8, 'EUR', 299.99),
    (9, 9, 'EUR', 229.99),
    (10, 10, 'EUR', 3999.99);

