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
SIGN = f"\n{DASH} View Product Prices {DASH}\n"

# ══════════ VIEW DATA ══════════════


#════ Retrieve Product Price ════


def view_data_prod_price_list_view():
    spa_stores = ""
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    try:
        query = """
            SELECT 
                p.product_id AS "Product ID", 
                p.product_name AS "Product Name", 
                p.category_id AS "Category ID", 
                c.category_name AS "Category Name", 
                p.details ->> 'brand' AS "Brand", 
                p.details ->> 'specs' AS "Specs",
                pr.price AS "Product Price",
                pr.currency AS "Currency",
                ARRAY(
                    SELECT value
                    FROM jsonb_each_text(p.details)
                ) AS other_values
            FROM 
                products p
            JOIN 
                categories c ON p.category_id = c.category_id
            JOIN
                prices pr ON p.product_id = pr.product_id;
    """
        CURSOR.execute(query)
        spa_stores = CURSOR.fetchall()
        if spa_stores:
            for row in spa_stores:
                print(f"""
Product ID           : {row[0]}
Product Name         : {row[1]}
Product Category ID  : {row[2]}
Category Name        : {row[3]}
Brand                : {row[4]}
Specs                : {row[5]}
Price                : {row[6]} {row[7]}
\n{DASH*3}
        """)
            input("\nPress 'enter' to exit ...\n")
    except (Exception, psycopg.DatabaseError) as error:
        print(print(f"Error while retrieving data: {error}"))
        time.sleep(3)


def view_data_prod_price_single_view():
    spa_stores = ""
    os.system('clear')
    try:
        query = """
            SELECT 
                p.product_id AS "Product ID", 
                p.product_name AS "Product Name", 
                p.category_id AS "Category ID", 
                c.category_name AS "Category Name", 
                p.details ->> 'brand' AS "Brand", 
                p.details ->> 'specs' AS "Specs",
                pr.price AS "Product Price",
                pr.currency AS "Currency",
                ARRAY(
                    SELECT value
                    FROM jsonb_each_text(p.details)
                ) AS other_values
            FROM 
                products p
            JOIN 
                categories c ON p.category_id = c.category_id
            JOIN
                prices pr ON p.product_id = pr.product_id;
    """
        CURSOR.execute(query)
        spa_stores = CURSOR.fetchall()

        for row in  spa_stores:
            print(f"""
{BANNER}\n{DB_CHECK}\n
{SIGN}
Product ID           : {row[0]}
Product Name         : {row[1]}
Product Category ID  : {row[2]}
Category Name        : {row[3]}
Brand                : {row[4]}
Specs                : {row[5]}
Price                : {row[6]} {row[7]}
\n{DASH*3}
        """)
            input("\nPress 'enter' to view more and to exit ...\n")
            os.system('clear')

    except (Exception, psycopg.DatabaseError) as error:
            print(f"Error while retrieving data: {error}")
            time.sleep(3)
  

#---- View Store Data -------

def view_product_prices():
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        view_data = input("Do you want to display product price data in list view ☞ enter ①  or ② in singel view: ")
        if view_data == '1':
            view_data_prod_price_list_view()   
        elif view_data == '2':
            view_data_prod_price_single_view()
        else:
            print("Invalid option to view Product Prices")
            time.sleep(3)

if __name__ == "__main__":
    view_product_prices()



#════ end code ════