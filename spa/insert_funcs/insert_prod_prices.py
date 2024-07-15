import os
import time
import psycopg
from spa.deco.spa_db_banner import spa_banner
from spa.connection.spa_db_connect import spa_db_connection
from spa.connection.spa_db_check_conn import spa_db_check_connection

CONNECT, CURSOR = spa_db_connection()
DB_CHECK = spa_db_check_connection()
BANNER = spa_banner()
DASH = 10*'═'
SIGN = f"\n{DASH} Insert Product Prices {DASH}\n"


def goback(back_to_front):
    input("\n ↩️ Press Enter to return to Insert Data menu... or CONTROL+C to exit program")
    back_to_front()


## ═════════ INSERT DATA ═════════════

#------ Diplay Store Name, Id, Product Name, Id, Category Name, Product details --------

def display_store_prod_data():
    try:
        select_query = """
    SELECT
        s.store_id AS "Store ID",
        s.store_name AS "Store Name",
        p.product_id AS "Product ID", 
        p.product_name AS "Product Name", 
        c.category_name AS "Category Name", 
        p.details AS "Product details"
    FROM
        stores s
    FULL JOIN    
        products p ON p.product_id = s.store_id
    FULL JOIN 
        categories c ON p.category_id = c.category_id
    FULL JOIN
        prices pr ON p.product_id = pr.product_id;

    """
        CURSOR.execute(select_query)
        rows = CURSOR.fetchall()
        print(f"\n{DASH} STORE PRODUCT INFO{DASH}\n")
        if rows:
            for row in rows:
              print(f"""
Store ID            : {row[0]}  
Store Name          : {row[1]} 
Product ID          : {row[2]}  
Product Name        : {row[3]}
Product Category    : {row[4]}
Product Details     : {row[5]}


        """)
        else:
            print("No product data found.")
    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while retrieving data: {error}")


#----- Insert Product Price Data --------


def insert_product_price_data():
    data = []
    while True:
        try:
            num_entries = int(input("Enter the number of price entries you want to input: "))
            break  
        except ValueError:
            print("\n❌ Only value number should be entered")
            time.sleep(2)

    if num_entries > 0:
        for _ in range(num_entries):
            os.system('clear')
            print(f"{BANNER}\n{DB_CHECK}\n")
            print(SIGN)
            print(f"\nPress Ctrl+C to cancel\n{'-'*25}\n")
            product_id = input("Enter Product ID: ")
            store_id = input("Enter Store ID: ")
            currency = input("Enter Currency (e.g EUR): ")
            price = input("Enter Product Price: ")
            data.append((product_id, store_id, currency, price))
    else:
        print("No product entries to input as the number entered is 0")


    query= """
    INSERT INTO prices(
        product_id, 
        store_id, 
        currency,
        price
        )
    VALUES(%s, %s, %s, %s)
    RETURNING *;
    """


    for entry in data:
            product_id, store_id, currency, price = entry

            CURSOR.execute(query,(product_id, store_id, currency, price))
        
    CONNECT.commit()
    print("\nPrice data succesfully inserted")

    select_query = """
        SELECT
            pr.product_id AS "Product ID",
            pr.store_id AS "Store ID",
            pr.currency AS "Currency",
            pr.price AS "Product Price"
        FROM
		    prices pr
	    WHERE pr.product_id = %s;
    """
    for entry in data:
        product_id, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (product_id,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for product name: {product_id}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED PRICE DATA {DASH}\n
Product ID           : {row[0]}
Store ID             : {row[1]}
Product currency     : {row[2]}
Product price        : {row[3]}

\n{DASH*3}
        """)
    time.sleep(10)


#----- Insert Product Price  --------

def insert_product_price(back_to_front):
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        view_data = input("Do you want to view all product category before insert data? (yes/no): ").strip().lower()
        if view_data == 'yes':
            display_store_prod_data()
            insert_product_price_data()
        elif view_data == 'no':
            goback(back_to_front)
        else:
            print("\n❌ Please give the option 'yes' or 'no'.")
            time.sleep(2)
            insert_product_price(back_to_front)   

