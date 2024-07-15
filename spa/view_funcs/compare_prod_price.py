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
SIGN = f"\n{DASH} Compare Product Prices {DASH}\n"

def goback(back_to_front):
    input("\n ↩️ Press Enter to return to View Data menu... or CONTROL+C to exit program")
    back_to_front()



# ══════════ VIEW DATA ══════════════


#════  Compare Product Price ════


def display_all_prod_cat():
    try:
        select_query = """
        SELECT *
        FROM categories;

    """
        CURSOR.execute(select_query)
        rows = CURSOR.fetchall()
        print(f"\n{DASH} PRODUCT CATEGORIES {DASH}\n")
        if rows:
            for row in rows:
                print(f"""
ID      : {row[0]}  
NAME    : {row[1]}
        """)
        else:
            print("No product data found.")
    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while retrieving data: {error}")


def compare_product_prices_data(back_to_front):
    data = []
    category_name = input("Enter Product Category name: ")
    if category_name:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
    
        data.append((category_name,))
    else:
        print("No category entries to input as the number entered is 0")
    query= """
        SELECT
            s.store_name,
            c.category_name,
            p.product_name,
            p.details,
            pr.price,
            pr.currency
        FROM stores s
        JOIN products p 
            ON s.store_id = p.product_id
        JOIN categories c
            ON p.category_id = c.category_id
        JOIN prices pr
            ON p.product_id = pr.product_id
        WHERE c.category_name = %s;
    """
    for entry in data:
        category_name = entry

        CURSOR.execute(query,(category_name))

        # Fetch all rows
        rows = CURSOR.fetchall()

        if not rows:
            print(f"No data found for category name: {category_name}")

# Print each row
        for row in rows:
            print(f"""
Store Name      : {row[0]}
Category Name   : {row[1]}
Product Name    : {row[2]}
Product Details : {row[3]}
Product Price   : {row[4]}
Price Currency  : {row[5]}

\n{DASH*3}
        """)
    goback(back_to_front)







def compare_product_prices(back_to_front):
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        view_data = input("Do you want to view all product category names before fetch data? (yes/no): ").strip().lower()
        if view_data == 'yes':
            display_all_prod_cat()
            compare_product_prices_data(back_to_front)
        elif view_data == 'no':
            goback(back_to_front)
        else:
            print("\n❌ Please give the option 'yes' or 'no'.")
            time.sleep(2)
            compare_product_prices(back_to_front)   


#════ end code ════