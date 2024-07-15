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
SIGN = f"\n{DASH} View Store Data {DASH}\n"

# ══════════ VIEW DATA ══════════════


#═══════ Retrieve Store Data ═══════

def view_data_stores_list_view():
    spa_stores = ""
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    try:
        query = """
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
        CURSOR.execute(query)
        spa_stores = CURSOR.fetchall()
        if spa_stores:
            for row in spa_stores:
                print(f"""
Store ID       : {row[0]}
Store Name     : {row[1]}
Store Type     : {row[2]}
Visit Store    : {row[3]}
Telephone      : {row[4]}
Email          : {row[5]}
\n{DASH*3}
        """)
            input("\nPress 'enter' to exit ...\n")
    except (Exception, psycopg.DatabaseError) as error:
        print(print(f"Error while retrieving data: {error}"))
        time.sleep(3)


def view_data_stores_single_view():
    spa_stores = ""
    os.system('clear')
    try:
        query = """
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
        CURSOR.execute(query)
        spa_stores = CURSOR.fetchall()

        for row in  spa_stores:
            print(f"""
{BANNER}\n{DB_CHECK}\n
{SIGN}
Store ID       : {row[0]}
Store Name     : {row[1]}
Store Type     : {row[2]}
Visit Store    : {row[3]}
Telephone      : {row[4]}
Email          : {row[5]}
\n{DASH*3}
        """)
            input("\nPress 'enter' to view more and to exit ...\n")
            os.system('clear')

    except (Exception, psycopg.DatabaseError) as error:
            print(f"Error while retrieving data: {error}")
            time.sleep(3)
  

#---- View Store Data -------

def view_data_stores():
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        view_data = input("Do you want to display store data in list view ☞ enter ①  or ② in singel view: ")
        if view_data == '1':
            view_data_stores_list_view()   
        elif view_data == '2':
            view_data_stores_single_view()
        else:
            print("Invalid option to view Store Data")
            time.sleep(3)

if __name__ == "__main__":
    view_data_stores()

