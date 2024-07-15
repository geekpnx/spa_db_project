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
SIGN = f"\n{DASH} Remove Store Data {DASH}\n"

def goback(back_to_front):
    input("\n ↩️ Press Enter to return to Insert Data menu... or CONTROL+C to exit program")
    back_to_front()


#======= Remove Store Data per value =========

def delete_store_data_by_name(store_name):
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    try:
        delete_query = "DELETE FROM stores WHERE store_name = %s"
        CURSOR.execute(delete_query, (store_name,))
        CONNECT.commit()
        if CURSOR.rowcount > 0:
            print(f"Store data for '{store_name}' deleted successfully")
            time.sleep(3)
        else:
            print(f"No store found with the name '{store_name}'")
            time.sleep(3)
    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while deleting data: {error}")
        time.sleep(3)


def delete_store_data_by_id(store_id):
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    try:
        delete_query = "DELETE FROM stores WHERE store_id = %s"
        CURSOR.execute(delete_query, (store_id,))
        CONNECT.commit()

        if CURSOR.rowcount > 0:
            print(f"Store data for ID '{store_id}' deleted successfully")
            time.sleep(3)
        else:
            print(f"No store found with the ID '{store_id}'")
            time.sleep(3)

    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while deleting data: {error}")
        time.sleep(3)

#---------- Display All Stores data ---------

def display_all_stores():
    try:
        select_query = """
        SELECT 
            store_id, 
            store_name, 
            location ->> 'type' AS "Store Location", 
            location ->> 'address' AS "Store Website",
            contact_info ->> 'telephone' AS "Telephone",
            contact_info ->> 'email' AS "Email",
            ARRAY(
                SELECT value
                FROM jsonb_each_text(location)
                WHERE key NOT IN ('type', 'address')
                UNION ALL
                SELECT value
                FROM jsonb_each_text(contact_info)
            ) AS other_values
        FROM stores;

    """
        CURSOR.execute(select_query)
        rows = CURSOR.fetchall()
        if rows:
            for row in rows:
                print(f"""
Store ID       : {row[0]}
Store Name     : {row[1]}
Store Type     : {row[2]}
Visit Store    : {row[3]}
Telephone      : {row[4]}
Email          : {row[5]}
\n{DASH*3}
        """)
        else:
            print("No store data found.")
    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error while retrieving data: {error}")



#------- Remove Store Data ----------------

def remove_store_data(back_to_front):
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        view_data = input("Do you want to view all store data before deletion? (yes/no): ").strip().lower()
        if view_data == 'yes':
            display_all_stores()
        elif view_data == 'no':
            goback(back_to_front)
        else:
            print("\n❌ Please give the option 'yes' or 'no'.")
            time.sleep(2)
            remove_store_data(back_to_front)
        delete = input("Do you want to delete any store data? (yes/no): ").strip().lower()
        if delete == 'yes':
            delete_by = input("Delete by name or ID? (name/id): ").strip().lower()
            if delete_by == 'name':
                store_name_to_delete = input("Enter the store name to delete: ").strip()
                delete_store_data_by_name(store_name_to_delete)
            elif delete_by == 'id':
                try:
                    store_id_to_delete = int(input("Enter the store ID to delete: ").strip())
                    delete_store_data_by_id(store_id_to_delete)
                except ValueError:
                    print(("Invalid ID entered. Please enter existing ID."))
            else:
                print("Invalid option for deletion")
                time.sleep(3)
        elif delete == 'no':
            goback(back_to_front)
        else:
            print("No deletion performed")
            time.sleep(3)

if __name__ == "__main__":
    remove_store_data()
