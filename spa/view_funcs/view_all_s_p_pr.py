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
SIGN = f"\n{DASH} View All Stores Products & Prices {DASH}\n"

def goback(back_to_front):
    input("\n ↩️ Press Enter to return to Insert Data menu... or CONTROL+C to exit program")
    back_to_front()

# ══════════ VIEW DATA ══════════════


#═══════ Retrieve Store Data ═══════

def view_all_s_p_pr_list_view():
    spa_stores = ""
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    try:
        query = """
            SELECT
                s.store_id,
                s.store_name,
                s.location,
                s.contact_info,
                p.product_id,
                p.product_name,
                p.details,
                c.category_id,
                c.category_name,
                pr.price,
                pr.currency
            FROM stores s
            JOIN products p 
                ON s.store_id = p.product_id
            JOIN categories c
                ON p.category_id = c.category_id
            JOIN prices pr
                ON p.product_id = pr.product_id;

    """
        CURSOR.execute(query)
        spa_stores = CURSOR.fetchall()
        if spa_stores:
            for row in spa_stores:
                print(f"""
Store ID               : {row[0]}
Store Name             : {row[1]}
Store Location         : {row[2]}
Store Contact Info     : {row[3]}
Product ID             : {row[4]}
Product Name           : {row[5]}
Product Details        : {row[6]}
Product Category ID    : {row[7]}
Product Category Name  : {row[8]}
Product Price          : {row[9]}
Price Currency         : {row[10]}

\n{DASH*3}
        """)
            input("\nPress 'enter' to exit ...\n")
    except (Exception, psycopg.DatabaseError) as error:
        print(print(f"Error while retrieving data: {error}"))
        time.sleep(3)


def view_all_s_p_pr_single_view():
    spa_stores = ""
    os.system('clear')
    try:
        query = """
            SELECT
                s.store_id,
                s.store_name,
                s.location,
                s.contact_info,
                p.product_id,
                p.product_name,
                p.details,
                c.category_id,
                c.category_name,
                pr.price,
                pr.currency
            FROM stores s
            JOIN products p 
                ON s.store_id = p.product_id
            JOIN categories c
                ON p.category_id = c.category_id
            JOIN prices pr
                ON p.product_id = pr.product_id;
    """
        CURSOR.execute(query)
        spa_stores = CURSOR.fetchall()

        for row in  spa_stores:
            print(f"""
{BANNER}\n{DB_CHECK}\n
{SIGN}
Store ID               : {row[0]}
Store Name             : {row[1]}
Store Location         : {row[2]}
Store Contact Info     : {row[3]}
Product ID             : {row[4]}
Product Name           : {row[5]}
Product Details        : {row[6]}
Product Category ID    : {row[7]}
Product Category Name  : {row[8]}
Product Price          : {row[9]}
Price Currency         : {row[10]}
\n{DASH*3}
        """)
            input("\nPress 'enter' to view more and to exit ...\n")
            os.system('clear')

    except (Exception, psycopg.DatabaseError) as error:
            print(f"Error while retrieving data: {error}")
            time.sleep(3)
  

#---- View Store Data -------

def view_all_s_p_pr_data(back_to_front):
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        view_data = input("Do you want to display all data in list view ☞ enter ①  or ② in singel view: ") 
        if view_data == '1':
                    view_all_s_p_pr_list_view()   
        elif view_data == '2':
                    view_all_s_p_pr_single_view()
        else:
            print("\n❌  Invalid option to view all Data")
            time.sleep(2)
            view_all_s_p_pr_data(back_to_front)

if __name__ == "__main__":
     view_all_s_p_pr_data()


