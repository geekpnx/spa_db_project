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
SIGN = f"\n{DASH} Remove Product Data {DASH}\n"


def goback(back_to_front):
    input("\n ↩️ Press Enter to return to Insert Data menu... or CONTROL+C to exit program")
    back_to_front()


#======= Remove Product Data =========


def delete_product_data_by_name(product_name):
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    try:
        delete_query = "DELETE FROM stores WHERE product_name = %s CASCADE"
        CURSOR.execute(delete_query, (product_name,))
        CONNECT.commit()
        if CURSOR.rowcount > 0:
            print(f"Product data for '{product_name}' deleted successfully")
            time.sleep(3)
        else:
            print(f"No product found with the name '{product_name}'")
            time.sleep(3)
    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while deleting data: {error}")
        time.sleep(3)


def delete_product_data_by_id(product_id):
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    try:
        delete_query = "DELETE FROM products WHERE product_id = %s"
        CURSOR.execute(delete_query, (product_id,))
        CONNECT.commit()

        if CURSOR.rowcount > 0:
            print(f"Product data for ID '{product_id}' deleted successfully")
            time.sleep(3)
        else:
            print(f"No product found with the ID '{product_id}'")
            time.sleep(3)

    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while deleting data: {error}")
        time.sleep(3)

#---------- Display All Stores data ---------

def display_all_products():
    try:
        select_query = """
        SELECT 
            product_id, 
            product_name, 
            category_id,
            details
        FROM products;
    """
        CURSOR.execute(select_query)
        rows = CURSOR.fetchall()
        if rows:
            for row in rows:
                print(f"""
Product ID      : {row[0]}
Product Name    : {row[1]}
Category ID     : {row[2]}
Product Details : {row[3]}
\n{DASH*3}
        """)
        else:
            print("No product data found.")
    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while retrieving data: {error}")



#------- Remove Store Data ----------------

def remove_product_data(back_to_front):
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        view_data = input("Do you want to view all product data before deletion? (yes/no): ").strip().lower()
        if view_data == 'yes':
            display_all_products()
        elif view_data == 'no':
            goback(back_to_front)
        else:
            print("\n❌ Please give the option 'yes' or 'no'.")
            time.sleep(2)
            remove_product_data(back_to_front)
        delete = input("Do you want to delete any product data? (yes/no): ").strip().lower()
        if delete == 'yes':
            delete_by = input("Delete by name or ID? (name/id): ").strip().lower()
            if delete_by == 'name':
                product_name_to_delete = input("Enter the product name to delete: ").strip()
                delete_product_data_by_name(product_name_to_delete)
            elif delete_by == 'id':
                try:
                    product_id_to_delete = int(input("Enter the product ID to delete: ").strip())
                    delete_product_data_by_id(product_id_to_delete)
                except ValueError:
                    print(("Invalid ID entered. Please enter existing ID."))
            else:
                print("Invalid option for deletion")
                time.sleep(3)
        else:
            print("No deletion performed")
            time.sleep(3)

if __name__ == "__main__":
    remove_product_data()
