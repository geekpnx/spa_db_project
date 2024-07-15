import sys
import os
import signal
import sys
import time


#----------- Register and Login --------

from spa.reglog_funcs.registration import register_user
from spa.reglog_funcs.login import login_user

#---------- All Inserts and Removes ------------
from spa.insert_funcs.insert_stores_pv import insert_store_data_per_value 
from spa.insert_funcs.remove_store_dt import remove_store_data
from spa.insert_funcs.insert_products_pv import insert_product_data_per_value
from spa.insert_funcs.remove_prod_dt import remove_product_data
from spa.insert_funcs.insert_prod_prices import insert_product_price
from spa.insert_funcs.remove_prod_price import remove_price_data
from spa.insert_funcs.insert_new_prod_cat import insert_new_prod_cat_dt
from spa.insert_funcs.remove_prod_cat import remove_prod_cat_data

#---------- All Views ------------
from spa.view_funcs.view_stores import view_data_stores
from spa.view_funcs.view_products import view_data_products 
from spa.view_funcs.view_prod_price import view_product_prices
from spa.view_funcs.view_prod_cat import view_product_category
from spa.view_funcs.compare_prod_price import compare_product_prices
from spa.view_funcs.view_all_s_p_pr import view_all_s_p_pr_data

#----- Database Connection -----
from spa.connection.spa_db_check_conn import spa_db_check_connection
from spa.connection.spa_db_connect import spa_db_connection


#-------- BANNER -------
from spa.deco.spa_db_banner import spa_banner

CONNECT, CURSOR = spa_db_connection()
DB_CHECK = spa_db_check_connection()
BANNER = spa_banner()

#---------- Keboard handling CTR + C -----------

def signal_handler(sig, frame):
        CURSOR.close()
        CONNECT.close()
        print("\n\n🔴 Database Offline & Disconnected")
        time.sleep(1)
        print("\nExiting program...\n")
        time.sleep(1)
        print("\nThank you for using SPA services\n")
        sys.exit(2) 
    
signal.signal(signal.SIGINT, signal_handler)

#-----------------------------------------------

#========= FRONT MENU ==========================
def entry_menu():
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        menu = f"""
Welcome, to SPA services.

Simple CLI application that can help you to collect, track 
and compare product prices from different stores.

Please, login or register if you haven't already.


═════════ ENTRY POINT ═════════


① ‣ REGISTER 

② ‣ LOGIN 

    """
        print(menu)
        select_menu = input(f"☞ Enter ①  ∘ ②  or 'q' to (quit): ")
    
        if select_menu == '1':
            register_user()
        elif select_menu == '2':
            login_user(main_menu)
        elif select_menu.lower() == 'q':
            CURSOR.close()
            CONNECT.close()
            print("\n🔴 Database Offline & Disconnected")
            time.sleep(1)
            print("\nExiting program...\n")
            time.sleep(1)
            print("\nThank you for using SPA services\n")
            sys.exit(2) 
        else:
            print(f"\n✖ Given number is not in the selection ✖\n")
            time.sleep(1)


def main_menu():
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        menu = f"""
═════════════ MAIN MENU ═════════════
        
① ‣ INSERT DATA   

② ‣ VIEW DATA     

    """
        print(menu)
        select_menu = input(f"☞ Enter ①  ∘ ②  or 'q' to (quit): ")
    
        if select_menu == '1':
            entry_data_menu()
        elif select_menu == '2':
            view_data_menu()
        elif select_menu.lower() == 'q':
            CURSOR.close()
            CONNECT.close()
            print("\n🔴 Database Offline & Disconnected")
            time.sleep(1)
            print("\nExiting program...\n")
            time.sleep(1)
            print("\nThank you for using SPA services\n")
            sys.exit(2) 
        else:
            print(f"\n✖ Given number is not in the selection ✖\n")
            time.sleep(1)


#═════════ INSERT DATA MENU ═════════════

def entry_data_menu():
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        menu = f"""

═════════════ INSERT DATA ═════════════


STORES ⤵
———————

① ‣ Insert Store Data per value        

② ‣ Remove Store Data 


PRODUCTS ⤵
—————————

③ ‣ Insert Product Data 

④ ‣ Remove Product Data	     

—————————

⑤ ‣ Insert Product Price 

⑥ ‣ Remove Product Price  
             

OTHERS ⤵
———————

⑦ ‣ Insert new Product Category   

⑧ ‣ Remove Product Category

————————
    """
        print(menu)
        select_menu = input("☞ Enter ① ∘ ② ∘ ③ ∘ ④ ∘ ⑤ ∘ ⑥ ∘ ⑦ ∘ ⑧ / 'f' to (go to main)  or 'q' to (quit): ")
        
        if select_menu == '1':
            insert_store_data_per_value()
        elif select_menu == '2':
            remove_store_data(entry_data_menu)
        elif select_menu == '3':
            insert_product_data_per_value(entry_data_menu)
        elif select_menu == '4':
            remove_product_data(entry_data_menu)
        elif select_menu == '5':
            insert_product_price(entry_data_menu)
        elif select_menu == '6':
            remove_price_data(entry_data_menu)
        elif select_menu == '7':
            insert_new_prod_cat_dt(entry_data_menu)
        elif select_menu == '8':
            remove_prod_cat_data(entry_data_menu)
        elif select_menu.lower() == 'f':
            main_menu()
        elif select_menu.lower() == 'q':
            CURSOR.close()
            CONNECT.close()
            print("\n🔴 Database Offline & Disconnected")
            time.sleep(1)
            print("\nExit program...\n")
            time.sleep(1)
            print("\nThank you for using SPA services\n")
            sys.exit() 
        else:
            print("\n✖ Given number is not in the selection ✖\n")
            time.sleep(1)


#═════════ VIEW DATA MENU ═════════════

def view_data_menu():
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        menu = f"""

═════════════ VIEW DATA ═════════════


STORES ⚯
—————————

① ‣ View Store Data           


PRODUCTS ⚯
———————————

② ‣ View Product Data         

③ ‣ View Product Prices   

④ ‣ View Product Categories          


OTHERS ⚯
————————

⑤ ‣ Compare Product Prices        

⑥ ‣ View All Stores, Products & Prices 

————————
    """
        print(menu)
        select_menu = input("☞ Enter ①  ∘ ②  ∘ ③  ∘ ④  ∘ ⑤  ∘ ⑥ / 'f' to (go to main)  or 'q' to (quit): ")
        
        if select_menu == '1':
            view_data_stores()
        elif select_menu == '2':
            view_data_products()
        elif select_menu == '3':
            view_product_prices()
        elif select_menu == '4':
            view_product_category()
        elif select_menu == '5':
            compare_product_prices(view_data_menu)
        elif select_menu == '6':
            view_all_s_p_pr_data(view_data_menu)
        elif select_menu.lower() == 'f':
            main_menu()
        elif select_menu.lower() == 'q':
            CURSOR.close()
            CONNECT.close()
            print("\n🔴 Database Offline & Disconnected")
            time.sleep(1)
            print("\nExiting program...\n")
            time.sleep(1)
            print("\nThank you for using SPA services\n")
            sys.exit() 
        else:
            print("\n✖ Given number is not in the selection ✖\n")
            time.sleep(1)


if __name__ == '__main__':
    entry_menu()
