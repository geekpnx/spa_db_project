-- login as postgres user

-- psql -U postgres

-- create user spa_admin

-- CREATE ROLE spa_admin WITH LOGIN SUPERUSER CREATEDB CREATEROLE PASSWORD 'password';

-- Switch to the user spa_admin

-- \c postgres spa_admin

-- Create the database

-- CREATE DATABASE spa_db;

-- Switch to the database
-- \c spa_db spa_admin

-- Create the stores table
CREATE TABLE stores(
    store_id SERIAL PRIMARY KEY,
    store_name VARCHAR(100) NOT NULL,
    location JSONB, -- e.g., {"type": "online", "address": "www.apple.com"} or {"type": "offline", "address": "Alexanderplatz. 1, 10178 Berlin"}
    contact_info JSONB -- e.g., {"telephone": "+491234567890", "email": "store@store.com"}
);


-- Create the categories table
CREATE TABLE categories(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50)
);

-- Create the products table
CREATE TABLE products(
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT REFERENCES categories(category_id),
    details JSONB -- e.g., {"brand": "Apple", "specs": {"CPU": "Apple M1", "GPU": "Apple M1", "ram": "16GB", "storage": "256GB SSD"}}
);

-- Create the prices table with CHECK constraint and DEFAULT timestamp
CREATE TABLE prices(
    price_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(product_id),
    store_id INT REFERENCES stores(store_id),
    currency VARCHAR(3) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    date_entry TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);



-- Create the users table for login
CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL, -- Store hashed passwords, not plain text
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);


-- Create the user_sessions table to track login status
CREATE TABLE user_sessions(
    session_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    logout_time TIMESTAMP,
    status VARCHAR(10) CHECK (status IN ('logged_in', 'logged_out')) NOT NULL
);
