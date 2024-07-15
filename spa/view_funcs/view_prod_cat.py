import os
import time
from psycopg import DatabaseError
from spa.deco.spa_db_banner import spa_banner
from spa.connection.spa_db_connect import spa_db_connection
from spa.connection.spa_db_check_conn import spa_db_check_connection

CONNECT, CURSOR = spa_db_connection()
DB_CHECK = spa_db_check_connection()
BANNER = spa_banner()
DASH = 10*'═'
SIGN = f"\n{DASH} View Product Categories {DASH}\n"

# ══════════ VIEW DATA ══════════════


#════ Retrieve Product Category ════

def view_product_category():
    os.system('clear')
    try:   
        spa_stores = ""
        select_query = """
        SELECT *
        FROM categories;

    """
        CURSOR.execute(select_query)
        spa_stores = CURSOR.fetchall()
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        if spa_stores:
            for row in spa_stores:
                print(f"""    
ID      : {row[0]}  
NAME    : {row[1]}
        """)
            input("\nPress 'enter' to exit ...\n")
            os.system('clear')
        else:
            print("No store data found.")
    except (Exception, DatabaseError) as error:
        print(f"Error while retrieving data: {error}")



#════ end code ════