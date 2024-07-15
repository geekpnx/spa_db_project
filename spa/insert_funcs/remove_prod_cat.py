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
SIGN = f"\n{DASH} Remove Product Category {DASH}\n"

def goback(back_to_front):
    input("\n ↩️ Press Enter to return to Insert Data menu... or CONTROL+C to exit program")
    back_to_front()


#======= Remove Product Category =========

def delete_prod_cat_data_by_id(category_id):
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    try:
        delete_query = "DELETE FROM categories WHERE category_id = %s"
        CURSOR.execute(delete_query, (category_id,))
        CONNECT.commit()
        if CURSOR.rowcount > 0:
            print(f"Product Category data for ID '{category_id}' deleted successfully")
            time.sleep(3)
        else:
            print(f"No product catagory data found with the ID '{category_id}'")
            time.sleep(3)
    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while deleting data: {error}")
        time.sleep(3)

#---------- Display All Product Category data ---------

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
            print("No product category data found.")
    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while retrieving data: {error}")

#------- Remove Store Data ----------------

def remove_prod_cat_data(back_to_front):
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        view_data = input("Do you want to view all category data before deletion? (yes/no): ").strip().lower()
        if view_data == 'yes':
            display_all_prod_cat()
        elif view_data == 'no':
            goback(back_to_front)
        else:
            print("\n❌ Please give the option 'yes' or 'no'.")
            time.sleep(2)
            remove_prod_cat_data(back_to_front)
        delete = input("Do you want to delete any product category data? (yes/no): ").strip().lower()
        if delete == 'yes':
                try:
                    category_id_to_delete = int(input("Enter the product category ID to delete: ").strip())
                    delete_prod_cat_data_by_id(category_id_to_delete)
                except ValueError:
                    print(("Invalid product category ID entered. Please enter existing product category ID."))
                    time.sleep(3)
        elif delete == 'no':
            goback(back_to_front)
        else:
            print("No deletion performed")
            time.sleep(3)

if __name__ == "__main__":
   remove_prod_cat_data()
