import os
import time
import json
import psycopg
from spa.deco.spa_db_banner import spa_banner
from spa.connection.spa_db_connect import spa_db_connection
from spa.connection.spa_db_check_conn import spa_db_check_connection



CONNECT, CURSOR = spa_db_connection()
DB_CHECK = spa_db_check_connection()
BANNER = spa_banner()
DASH = 10*'═'
SIGN = f"\n{DASH} Insert Product Data per value {DASH}\n"

def goback(back_to_front):
    input("\n ↩️ Press Enter to return to Insert Data menu... or CONTROL+C to exit program")
    back_to_front()
    



#======= Insert Product Data per value =========

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


#------ 1 Laptop ------------------
def insert_product_data_laptop():

    data = []
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        try:
            num_entries = int(input("Enter the number of product entries you want to input for AR Glasses: "))
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
            product_name = input("Enter product name: ")
            category_id = 1
            detail_brand = input("Enter product brand: ")
            detail_spec_cpu = input("Enter product CPU spec: ")
            detail_spec_gpu = input("Enter product GPU spec: ")
            detail_spec_ram = input("Enter product RAM spec: ")
            detail_spec_strg = input("Enter product Storage size (GB/TB) and type (SSD/HHD) spec: ")
            data.append((product_name, category_id, detail_brand, detail_spec_cpu, detail_spec_gpu, detail_spec_ram, detail_spec_strg))
    else:
        print("No product entries to input as the number entered is 0")

    query= """
    INSERT INTO products(
        product_name, 
        category_id, 
        details
        )
    VALUES(%s, %s, %s)
    RETURNING *;
    """

    for entry in data:
        product_name, category_id, detail_brand, detail_spec_cpu, detail_spec_gpu, detail_spec_ram, detail_spec_strg = entry
        details = json.dumps({"brand": detail_brand, "specs": {"CPU": detail_spec_cpu, "GPU": detail_spec_gpu, "ram": detail_spec_ram, "storage" : detail_spec_strg}})


        CURSOR.execute(query,(product_name, category_id, details))
    
    CONNECT.commit()
    print("\n\Product data succesfully inserted")

    select_query = """
        SELECT 
            product_id, 
            product_name,
            category_id,
            details ->> 'brand' AS "Brand", 
            details -> 'specs' ->> 'CPU'  AS "CPU spec",
            details -> 'specs' ->> 'GPU'  AS "GPU spec",
            details -> 'specs' ->> 'ram'  AS "Ram spec",
            details -> 'specs' ->> 'storage'  AS "Storage spec",
            ARRAY(
                SELECT value
                FROM jsonb_each_text(details)
            ) AS other_values
        FROM products
        WHERE category_id = %s;
    """ 

    for entry in data:
        _, category_id, _, _, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (category_id,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for product name: {category_id}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED PRODUCT DATA {DASH}\n
Product ID           : {row[0]}
Product Name         : {row[1]}
Product category ID  : {row[2]}
Product Brand        : {row[3]}
Product CPU spec     : {row[4]}
Product GPU spec     : {row[5]}
Product RAM spec     : {row[6]}
Product STORAGE spec : {row[7]}
\n{DASH*3}
        """)
    time.sleep(10)

#------ 2 Smartphone ------------------
def insert_product_data_smartphone():

    data = []
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        try:
            num_entries = int(input("Enter the number of product entries you want to input for AR Glasses: "))
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
            product_name = input("Enter product name: ")
            category_id = 2
            detail_brand = input("Enter product brand: ")
            detail_spec_cpu = input("Enter product CPU spec: ")
            detail_spec_gpu = input("Enter product GPU spec: ")
            detail_spec_ram = input("Enter product RAM spec: ")
            detail_spec_strg = input("Enter product Storage size (GB/TB) and type (SSD/HHD) spec: ")
            data.append((product_name, category_id, detail_brand, detail_spec_cpu, detail_spec_gpu, detail_spec_ram,detail_spec_strg))
    else:
        print("No product entries to input as the number entered is 0")
    query= """
    INSERT INTO products(
        product_name, 
        category_id, 
        details
        )
    VALUES(%s, %s, %s)
    RETURNING *;
    """

    for entry in data:
        product_name, category_id, detail_brand, detail_spec_cpu, detail_spec_gpu, detail_spec_ram, detail_spec_strg = entry
        details = json.dumps({"brand": detail_brand, "specs": {"CPU": detail_spec_cpu, "GPU": detail_spec_gpu, "ram": detail_spec_ram, "storage" : detail_spec_strg}})


        CURSOR.execute(query,(product_name, category_id, details))
    
    CONNECT.commit()
    print("\n\nproduct data succesfully inserted")

    select_query = """
        SELECT 
            product_id, 
            product_name,
            category_id,
            details ->> 'brand' AS "Brand", 
            details -> 'specs' ->> 'CPU'  AS "CPU spec",
            details -> 'specs' ->> 'GPU'  AS "GPU spec",
            details -> 'specs' ->> 'ram'  AS "Ram spec",
            details -> 'specs' ->> 'storage'  AS "Storage spec",
            ARRAY(
                SELECT value
                FROM jsonb_each_text(details)
            ) AS other_values
        FROM products
        WHERE category_id = %s;
    """ 

    for entry in data:
        _, category_id, _, _, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (category_id,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for product name: {category_id}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED PRODUCT DATA {DASH}\n
Product ID           : {row[0]}
Product Name         : {row[1]}
Product category ID  : {row[2]}
Product Brand        : {row[3]}
Product CPU spec     : {row[4]}
Product GPU spec     : {row[5]}
Product RAM spec     : {row[6]}
Product STORAGE spec : {row[7]}
\n{DASH*3}
        """)
    time.sleep(10)

#------ 3 tablet ------------------
def insert_product_data_tablet():

    data = []
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        try:
            num_entries = int(input("Enter the number of product entries you want to input for Tablet: "))
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
            product_name = input("Enter product name: ")
            category_id = 3
            detail_brand = input("Enter product brand: ")
            detail_spec_cpu = input("Enter product CPU spec: ")
            detail_spec_gpu = input("Enter product GPU spec: ")
            detail_spec_ram = input("Enter product RAM spec: ")
            detail_spec_strg = input("Enter product Storage size (GB/TB) and type (SSD/HHD) spec: ")
            data.append((product_name, category_id, detail_brand, detail_spec_cpu, detail_spec_gpu, detail_spec_ram,detail_spec_strg))
        else:
            print("No product entries to input as the number entered is 0")

    query= """
    INSERT INTO products(
        product_name, 
        category_id, 
        details
        )
    VALUES(%s, %s, %s)
    RETURNING *;
    """

    for entry in data:
        product_name, category_id, detail_brand, detail_spec_cpu, detail_spec_gpu, detail_spec_ram, detail_spec_strg = entry
        details = json.dumps({"brand": detail_brand, "specs": {"CPU": detail_spec_cpu, "GPU": detail_spec_gpu, "ram": detail_spec_ram, "storage" : detail_spec_strg}})


        CURSOR.execute(query,(product_name, category_id, details))
    
    CONNECT.commit()
    print("\n\nProduct data succesfully inserted")

    select_query = """
        SELECT 
            product_id, 
            product_name,
            category_id,
            details ->> 'brand' AS "Brand", 
            details -> 'specs' ->> 'CPU'  AS "CPU spec",
            details -> 'specs' ->> 'GPU'  AS "GPU spec",
            details -> 'specs' ->> 'ram'  AS "Ram spec",
            details -> 'specs' ->> 'storage'  AS "Storage spec",
            ARRAY(
                SELECT value
                FROM jsonb_each_text(details)
            ) AS other_values
        FROM products
        WHERE category_id = %s;
    """ 

    for entry in data:
        _, category_id, _, _, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (category_id,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for category ID: {category_id}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED PRODUCT DATA {DASH}\n
Product ID           : {row[0]}
Product Name         : {row[1]}
Product category ID  : {row[2]}
Product Brand        : {row[3]}
Product CPU spec     : {row[4]}
Product GPU spec     : {row[5]}
Product RAM spec     : {row[6]}
Product STORAGE spec : {row[7]}
\n{DASH*3}
        """)
    time.sleep(10)

#------ 4 PC ------------------
def insert_product_data_pc():

    data = []
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        try:
            num_entries = int(input("Enter the number of product entries you want to input for PC: "))
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
            product_name = input("Enter product name: ")
            category_id = 4
            detail_brand = input("Enter product brand: ")
            detail_spec_cpu = input("Enter product CPU spec: ")
            detail_spec_gpu = input("Enter product GPU spec: ")
            detail_spec_ram = input("Enter product RAM spec: ")
            detail_spec_strg = input("Enter product Storage size (GB/TB) and type (SSD/HHD) spec: ")
            data.append((product_name, category_id, detail_brand, detail_spec_cpu, detail_spec_gpu, detail_spec_ram,detail_spec_strg))
        else:
            print("No product entries to input as the number entered is 0")

    query= """
    INSERT INTO products(
        product_name, 
        category_id, 
        details
        )
    VALUES(%s, %s, %s)
    RETURNING *;
    """

    for entry in data:
        product_name, category_id, detail_brand, detail_spec_cpu, detail_spec_gpu, detail_spec_ram, detail_spec_strg = entry
        details = json.dumps({"brand": detail_brand, "specs": {"CPU": detail_spec_cpu, "GPU": detail_spec_gpu, "ram": detail_spec_ram, "storage" : detail_spec_strg}})


        CURSOR.execute(query,(product_name, category_id, details))
    
    CONNECT.commit()
    print("\n\nproduct data succesfully inserted")

    select_query = """
        SELECT 
            product_id, 
            product_name,
            category_id,
            details ->> 'brand' AS "Brand", 
            details -> 'specs' ->> 'CPU'  AS "CPU spec",
            details -> 'specs' ->> 'GPU'  AS "GPU spec",
            details -> 'specs' ->> 'ram'  AS "Ram spec",
            details -> 'specs' ->> 'storage'  AS "Storage spec",
            ARRAY(
                SELECT value
                FROM jsonb_each_text(details)
            ) AS other_values
        FROM products
        WHERE category_id = %s;
    """ 

    for entry in data:
        _, category_id, _, _, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (category_id,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for product name: {category_id}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED PRODUCT DATA {DASH}\n
Product ID           : {row[0]}
Product Name         : {row[1]}
Product category ID  : {row[2]}
Product Brand        : {row[3]}
Product CPU spec     : {row[4]}
Product GPU spec     : {row[5]}
Product RAM spec     : {row[6]}
Product STORAGE spec : {row[7]}
\n{DASH*3}
        """)
    time.sleep(10)

#------ 5 speakers w ------------------
def insert_product_data_speakers_w():

    data = []
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        try:
            num_entries = int(input("Enter the number of product entries you want to input for Speakers Wire: "))
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
            product_name = input("Enter product name: ")
            category_id = 5
            detail_brand = input("Enter product brand: ")
            detail_spec_conn = "Wire"
            detail_spec_type = input("Enter product Type (active/passive) spec: ")
            data.append((product_name, category_id, detail_brand, detail_spec_conn, detail_spec_type))
    else:
        print("No product entries to input as the number entered is 0")

    query= """
    INSERT INTO products(
        product_name, 
        category_id, 
        details
        )
    VALUES(%s, %s, %s)
    RETURNING *;
    """

    for entry in data:
        product_name, category_id, detail_brand, detail_spec_conn, detail_spec_type = entry
        details = json.dumps({"brand": detail_brand, "specs": {"connection": detail_spec_conn, "type": detail_spec_type}})


        CURSOR.execute(query,(product_name, category_id, details))
    
    CONNECT.commit()
    print("\n\nproduct data succesfully inserted")

    select_query = """
        SELECT 
            product_id, 
            product_name,
            category_id,
            details ->> 'brand' AS "Brand", 
            details -> 'specs' ->> 'connection'  AS "Connection spec",
            details -> 'specs' ->> 'type'  AS "Type spec",
            ARRAY(
                SELECT value
                FROM jsonb_each_text(details)
            ) AS other_values
        FROM products
        WHERE category_id = %s;
    """ 

    for entry in data:
        _, category_id, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (category_id,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for product name: {category_id}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED PRODUCT DATA {DASH}\n
Product ID              : {row[0]}
Product Name            : {row[1]}
Product category ID     : {row[2]}
Product Brand           : {row[3]}
Product Connection spec : {row[4]}
Product Type spec       : {row[5]}
\n{DASH*3}
        """)
    time.sleep(10)

#------ 6 speakers wl ------------------
def insert_product_data_speakers_wl():

    data = []
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        try:
            num_entries = int(input("Enter the number of product entries you want to input for Speakers Wireless: "))
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
            product_name = input("Enter product name: ")
            category_id = 6
            detail_brand = input("Enter product brand: ")
            detail_spec_conn = "Wireless"
            detail_spec_type = input("Enter product Type (active/passive) spec: ")
            data.append((product_name, category_id, detail_brand, detail_spec_conn, detail_spec_type))
    else:
        print("No product entries to input as the number entered is 0")

    query= """
    INSERT INTO products(
        product_name, 
        category_id, 
        details
        )
    VALUES(%s, %s, %s)
    RETURNING *;
    """

    for entry in data:
        product_name, category_id, detail_brand, detail_spec_conn, detail_spec_type = entry
        details = json.dumps({"brand": detail_brand, "specs": {"connection": detail_spec_conn, "type": detail_spec_type}})


        CURSOR.execute(query,(product_name, category_id, details))
    
    CONNECT.commit()
    print("\n\nproduct data succesfully inserted")

    select_query = """
        SELECT 
            product_id, 
            product_name,
            category_id,
            details ->> 'brand' AS "Brand", 
            details -> 'specs' ->> 'connection'  AS "Connection spec",
            details -> 'specs' ->> 'type'  AS "Type spec",
            ARRAY(
                SELECT value
                FROM jsonb_each_text(details)
            ) AS other_values
        FROM products
        WHERE category_id = %s;
    """ 

    for entry in data:
        _, category_id, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (category_id,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for product name: {category_id}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED PRODUCT DATA {DASH}\n
Product ID              : {row[0]}
Product Name            : {row[1]}
Product category ID     : {row[2]}
Product Brand           : {row[3]}
Product Connection spec : {row[4]}
Product Type spec       : {row[5]}
\n{DASH*3}
        """)
    time.sleep(10)

#------ 7 headphones w ------------------
def insert_product_data_headphones_w():

    data = []
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        try:
            num_entries = int(input("Enter the number of product entries you want to input for Headphones Wire: "))
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
            product_name = input("Enter product name: ")
            category_id = 7
            detail_brand = input("Enter product brand: ")
            detail_spec_conn = "Wire"
            detail_spec_type = input("Enter product Type (over/on/in-ear) spec: ")
            detail_spec_noise_cancel = input("Enter product Noise Canceling (yes/no) spec: ")
            data.append((product_name, category_id, detail_brand, detail_spec_conn, detail_spec_type, detail_spec_noise_cancel))
        else:
            print("No product entries to input as the number entered is 0")

    query= """
    INSERT INTO products(
        product_name, 
        category_id, 
        details
        )
    VALUES(%s, %s, %s)
    RETURNING *;
    """

    for entry in data:
        product_name, category_id, detail_brand,detail_spec_conn, detail_spec_type, detail_spec_noise_cancel = entry
        details = json.dumps({"brand": detail_brand, "specs": {"connection": detail_spec_conn, "type": detail_spec_type,"noise_canceling": detail_spec_noise_cancel}})


        CURSOR.execute(query,(product_name, category_id, details))
    
    CONNECT.commit()
    print("\n\nproduct data succesfully inserted")

    select_query = """
        SELECT 
            product_id, 
            product_name,
            category_id,
            details ->> 'brand' AS "Brand", 
            details -> 'specs' ->> 'connection' AS "Connection spec",
            details -> 'specs' ->> 'type' AS "Type spec",
            details -> 'specs' ->> 'noise_canceling' AS "Noise Canceling spec",
            ARRAY(
                SELECT value
                FROM jsonb_each_text(details)
            ) AS other_values
        FROM products
        WHERE category_id = %s;
    """ 

    for entry in data:
        _, category_id, _, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (category_id,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for product name: {category_id}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED PRODUCT DATA {DASH}\n
Product ID                      : {row[0]}
Product Name                    : {row[1]}
Product category ID             : {row[2]}
Product Brand                   : {row[3]}
Product Connection spec         : {row[4]}
Product Type spec               : {row[5]}
Product Noise Canceling spec    : {row[6]}
\n{DASH*3}
        """)
    time.sleep(10)

#------ 8 headphones wl ------------------

def insert_product_data_headphones_wl():

    data = []
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        try:
            num_entries = int(input("Enter the number of product entries you want to input for Headphones Wireless: "))
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
            product_name = input("Enter product name: ")
            category_id = 8
            detail_brand = input("Enter product brand: ")
            detail_spec_conn = "Wireless"
            detail_spec_type = input("Enter product Type (over/on/in-ear) spec: ")
            detail_spec_noise_cancel = input("Enter product Noise Canceling (yes/no) spec: ")
            detail_spec_battery = input("Enter product Noise Battery (time in hour) spec: ")
            data.append((product_name, category_id, detail_brand, detail_spec_conn, detail_spec_type, detail_spec_noise_cancel,detail_spec_battery))
    else:
        print("No product entries to input as the number entered is 0")



    query= """
    INSERT INTO products(
        product_name, 
        category_id, 
        details
        )
    VALUES(%s, %s, %s)
    RETURNING *;
    """

    for entry in data:
        product_name, category_id, detail_brand,detail_spec_conn, detail_spec_type, detail_spec_noise_cancel,detail_spec_battery = entry
        details = json.dumps({"brand": detail_brand, "specs": {"connection": detail_spec_conn, "type": detail_spec_type,"noise_canceling": detail_spec_noise_cancel,"battery": detail_spec_battery}})


        CURSOR.execute(query,(product_name, category_id, details))
    
    CONNECT.commit()
    print("\n\nproduct data succesfully inserted")

    select_query = """
        SELECT 
            product_id, 
            product_name,
            category_id,
            details ->> 'brand' AS "Brand", 
            details -> 'specs' ->> 'connection' AS "Connection spec",
            details -> 'specs' ->> 'type' AS "Type spec",
            details -> 'specs' ->> 'noise_canceling' AS "Noise Canceling spec",
            details -> 'specs' ->> 'battery' AS "Battery spec",
            ARRAY(
                SELECT value
                FROM jsonb_each_text(details)
            ) AS other_values
        FROM products
        WHERE category_id = %s;
    """ 

    for entry in data:
        _, category_id, _, _, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (category_id,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for product name: {category_id}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED PRODUCT DATA {DASH}\n
Product ID                      : {row[0]}
Product Name                    : {row[1]}
Product category ID             : {row[2]}
Product Brand                   : {row[3]}
Product Connection spec         : {row[4]}
Product Type spec               : {row[5]}
Product Noise Canceling spec    : {row[6]}
Product Battery spec            : {row[7]}
\n{DASH*3}
        """)
    time.sleep(10)


#------ 9 earbuds ------------------

def insert_product_data_earbuds():

    data = []
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        try:
            num_entries = int(input("Enter the number of product entries you want to input for Earbuds: "))
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
            product_name = input("Enter product name: ")
            category_id = 9
            detail_brand = input("Enter product brand: ")
            detail_spec_battery = input("Enter product Battery (time in hour) spec: ")
            detail_spec_wireless = input("Enter product Wireless (yes/no) spec: ")
            detail_spec_noise_cancel = input("Enter product Noise Canceling (yes/no) spec: ")
    
            data.append((product_name, category_id, detail_brand, detail_spec_battery, detail_spec_wireless, detail_spec_noise_cancel))
        else:
            print("No product entries to input as the number entered is 0")
    query= """
    INSERT INTO products(
        product_name, 
        category_id, 
        details
        )
    VALUES(%s, %s, %s)
    RETURNING *;
    """

    for entry in data:
        product_name, category_id, detail_brand, detail_spec_battery, detail_spec_wireless, detail_spec_noise_cancel = entry
        details = json.dumps({"brand": detail_brand, "specs": {"battery": detail_spec_battery, "wireless": detail_spec_wireless,"noise_canceling": detail_spec_noise_cancel}})


        CURSOR.execute(query,(product_name, category_id, details))
    
    CONNECT.commit()
    print("\nProduct data succesfully inserted")

    select_query = """
        SELECT 
            product_id, 
            product_name,
            category_id,
            details ->> 'brand' AS "Brand", 
            details -> 'specs' ->> 'battery' AS "Battery spec",
            details -> 'specs' ->> 'wireless' AS "Wireless spec",
            details -> 'specs' ->> 'noise_canceling' AS "Noise Canceling spec",
            ARRAY(
                SELECT value
                FROM jsonb_each_text(details)
            ) AS other_values
        FROM products
        WHERE category_id = %s;
    """ 

    for entry in data:
        _, category_id, _, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (category_id,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for product name: {category_id}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED PRODUCT DATA {DASH}\n
Product ID                      : {row[0]}
Product Name                    : {row[1]}
Product category ID             : {row[2]}
Product Brand                   : {row[3]}
Product Battery spec            : {row[4]}
Product Wireless spec           : {row[5]}
Product Noise Canceling spec    : {row[6]}
\n{DASH*3}
        """)
    time.sleep(10)


#------ 10 AR Glasses ------------------

def insert_product_data_ar_glasses():

    data = []
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        try:
            num_entries = int(input("Enter the number of product entries you want to input for AR Glasses: "))
            break  
        except ValueError:
            print("\n❌ Only value number should be entered")
            time.sleep(2)

    if num_entries > 0:
        for _ in range(num_entries):
            os.system('clear')
            print(f"{BANNER}\n{DB_CHECK}\n")
            print(SIGN)
            print(f"\nPress CONTROL+C to close program\n{'-'*25}\n")
            product_name = input("Enter product name: ")
            category_id = 10
            detail_brand = input("Enter product brand: ")
            detail_spec_tracking = input("Enter product Tracking (inside_out) spec: ")
            detail_spec_resolution = input("Enter product Resolution (e.g 2048x1080) spec: ")
            detail_spec_field_of_view = input("Enter product Field Of View (e.g 52 degrees) spec: ")
    
            data.append((product_name, category_id, detail_brand, detail_spec_tracking, detail_spec_resolution, detail_spec_field_of_view))
    else:
        print("No product entries to input as the number entered is 0")


    query= """
    INSERT INTO products(
        product_name, 
        category_id, 
        details
        )
    VALUES(%s, %s, %s)
    RETURNING *;
    """

    for entry in data:
        product_name, category_id, detail_brand, detail_spec_tracking, detail_spec_resolution, detail_spec_field_of_view = entry
        details = json.dumps({"brand": detail_brand, "specs": {"tracking": detail_spec_tracking, "resolution": detail_spec_resolution,"field_of_view": detail_spec_field_of_view}})


        CURSOR.execute(query,(product_name, category_id, details))
    
    CONNECT.commit()
    print("\n\nProduct data succesfully inserted")

    select_query = """
        SELECT 
            product_id, 
            product_name,
            category_id,
            details ->> 'brand' AS "Brand", 
            details -> 'specs' ->> 'tracking' AS "Tracking spec",
            details -> 'specs' ->> 'resolution' AS "Wireless spec",
            details -> 'specs' ->> 'field_of_view' AS "Fiels Of View spec",
            ARRAY(
                SELECT value
                FROM jsonb_each_text(details)
            ) AS other_values
        FROM products
        WHERE category_id = %s;
    """ 

    for entry in data:
        _, category_id, _, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (category_id,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for product name: {category_id}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} INSERTED PRODUCT DATA {DASH}\n
Product ID                      : {row[0]}
Product Name                    : {row[1]}
Product category ID             : {row[2]}
Product Brand                   : {row[3]}
Product Tracking spec           : {row[4]}
Product Resolution spec         : {row[5]}
Product Field Of View spec      : {row[6]}
\n{DASH*3}
        """)
    time.sleep(10)


#-------------------------------------------------

#------- Insert Product Data menu ----------------

def insert_product_data_per_value(back_to_front):
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        view_data = input("Do you want to view all product category before insert data? (yes/no): ").strip().lower()
        if view_data == 'yes':
            display_all_prod_cat()
        elif view_data == 'no':
            goback(back_to_front)
        else:
            print("\n❌ Please give the option 'yes' or 'no'.")
            time.sleep(2)
            insert_product_data_per_value(back_to_front)   
        enter_option = input("☞ Enter Product Catergory ID: ").strip().lower()
        if enter_option == '1':
                insert_product_data_laptop()
        if enter_option == '2':
                insert_product_data_smartphone()
        if enter_option == '3':
                insert_product_data_tablet()
        if enter_option == '4':
                insert_product_data_pc()
        if enter_option == '5':
                insert_product_data_speakers_w()
        if enter_option == '6':
                insert_product_data_speakers_wl()
        if enter_option == '7':
                insert_product_data_headphones_w()
        if enter_option == '8':
                insert_product_data_headphones_wl()
        if enter_option == '9':
                insert_product_data_earbuds()
        if enter_option == '10':
                insert_product_data_ar_glasses()
        else:
            print("No insertion performed")
            time.sleep(3)





