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
SIGN = f"\n{DASH} Remove Product Price {DASH}\n"


def goback(back_to_front):
    input("\n ↩️ Press Enter to return to Insert Data menu... or CONTROL+C to exit program")
    back_to_front()


#======= Remove Product Price =========

def delete_price_data_by_id(price_id):
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    try:
        delete_query = "DELETE FROM prices WHERE price_id = %s"
        CURSOR.execute(delete_query, (price_id,))
        CONNECT.commit()
        if CURSOR.rowcount > 0:
            print(f"Price data for ID '{price_id}' deleted successfully")
            time.sleep(3)
        else:
            print(f"No price data found with the ID '{price_id}'")
            time.sleep(3)
    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while deleting data: {error}")
        time.sleep(3)


#---------- Display All Stores data ---------

def display_all_prices():
    try:
        select_query = """
        SELECT 
            price_id, 
            product_id, 
            store_id,
            currency,
            price,
            date_entry
        FROM prices;

    """
        CURSOR.execute(select_query)
        rows = CURSOR.fetchall()
        if rows:
            for row in rows:
                print(f"""
Price ID       : {row[0]}
Product ID     : {row[1]}
Store ID       : {row[2]}
Currency       : {row[3]}
Price          : {row[4]}
Date Entry     : {row[5]}
\n{DASH*3}
        """)
        else:
            print("No store data found.")
    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while retrieving data: {error}")
        time.sleep(3)

#------- Remove Store Data ----------------

def remove_price_data(back_to_front):
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        view_data = input("Do you want to view all price data before deletion? (yes/no): ").strip().lower()
        if view_data == 'yes':
            display_all_prices()
        elif view_data == 'no':
            goback(back_to_front)
        else:
            print("\n❌ Please give the option 'yes' or 'no'.")
            time.sleep(2)
            remove_price_data(back_to_front)
        delete = input("Do you want to delete any price data? (yes/no): ").strip().lower()
        if delete == 'yes':
                try:
                    price_id_to_delete = int(input("Enter the price ID to delete: ").strip())
                    delete_price_data_by_id(price_id_to_delete)
                except ValueError:
                    print(("Invalid price ID entered. Please enter existing price ID."))
                    time.sleep(3)
        elif delete == 'no':
            goback(back_to_front)
        else:
            print("No deletion performed")
            time.sleep(3)

if __name__ == "__main__":
    remove_price_data()
