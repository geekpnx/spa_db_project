import os
import time
import psycopg
from spa.deco.spa_db_banner import spa_banner
from spa.connection.spa_db_connect import spa_db_connection
from spa.connection.spa_db_check_conn import spa_db_check_connection
from spa.connection.spa_db_check_conn import spa_db_check_connection


CONNECT, CURSOR = spa_db_connection()
DB_CHECK = spa_db_check_connection()
BANNER = spa_banner()
DASH = 10*'═'
SIGN = f"\n{DASH} Insert New Product Category {DASH}\n"

def goback(back_to_front):
    input("\n ↩️ Press Enter to return to Insert Data menu... or CONTROL+C to exit program")
    back_to_front()



## ═════════ INSERT DATA ═════════════


#══════ Insert New Product Category ══════ 


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



def insert_prod_cat_data():
    data = []
    while True:
        try:
            num_entries = int(input("Enter the number of category entries you want to input: "))
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
            category_name = input("Enter New Product Category name: ")
            data.append((category_name,))
    else:
        print("No category entries to input as the number entered is 0")
    query= """
    INSERT INTO categories(
        category_name
        )
    VALUES(%s)
    RETURNING *;
    """

    for entry in data:
            category_name = entry

            CURSOR.execute(query,(category_name))
        
    CONNECT.commit()
    print("\nCategory data succesfully inserted")

    select_query = """
        SELECT
            category_name AS "Category Name"
        FROM
		    categories
	    WHERE category_name = %s;
    """
    for entry in data:
        category_name = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (category_name))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for category name: {category_name}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED NEW PRODUCT CATEGORY DATA {DASH}\n
Category Name   : {row[0]}

\n{DASH*3}
        """)
    time.sleep(10)


#----- Insert Product Price  --------

def insert_new_prod_cat_dt(back_to_front):
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        view_data = input("Do you want to view all product category before insert data? (yes/no): ").strip().lower()
        if view_data == 'yes':
            display_all_prod_cat()
            insert_prod_cat_data()
        elif view_data == 'no':
            goback(back_to_front)
        else:
            print("\n❌ Please give the option 'yes' or 'no'.")
            time.sleep(2)
            insert_new_prod_cat_dt(back_to_front)   



#══════ end code ══════ 
