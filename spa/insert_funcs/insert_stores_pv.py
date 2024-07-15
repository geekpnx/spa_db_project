import os
import time
import json
from spa.deco.spa_db_banner import spa_banner
from spa.connection.spa_db_connect import spa_db_connection
from spa.connection.spa_db_check_conn import spa_db_check_connection


CONNECT, CURSOR = spa_db_connection()
DB_CHECK = spa_db_check_connection()
BANNER = spa_banner()
DASH = 10*'═'
SIGN = f"\n{DASH} Insert Store Data per value {DASH}\n"

def goback(back_to_front):
    input("\n ↩️ Press Enter to return to Insert Data menu... or CONTROL+C to exit program")
    back_to_front()

# ═════════ INSERT DATA ═════════════


#======= Insert Store Data per value =========


def insert_store_data_per_value():

    data = []
    os.system('clear')
    print(BANNER)
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        try:
            num_entries = int(input("Enter the number of store entries you want to input: "))
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
            store_name = input("Enter store name: ")
            location_type = input("Enter location type (e.g., online, offline): ")
            location_address = input("Enter location address (e.g website (www.), street (Street address)): ")
            contact_telephone = input("Enter contact telephone (+49): ")
            contact_email = input("Enter contact email: ")
            data.append((store_name, location_type, location_address, contact_telephone, contact_email))
    else:
        print("No product entries to input as the number entered is 0")

    query= """
    INSERT INTO stores(
        store_name, 
        location, 
        contact_info
        )
    VALUES(%s, %s, %s)
    RETURNING *;
    """

    for entry in data:
        store_name, location_type, location_address, contact_telephone, contact_email = entry
        location = json.dumps({"type": location_type, "address": location_address})
        contact_info = json.dumps({"telephone": contact_telephone, "email": contact_email})

        CURSOR.execute(query,(store_name, location, contact_info))
    
    CONNECT.commit()
    print("\n\nStore data succesfully inserted")

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
        FROM stores
        WHERE store_name = %s;

    """ 

    for entry in data:
        store_name, _, _, _, _ = entry
        
        # Execute the select query
        CURSOR.execute(select_query, (store_name,))
        
        # Fetch all rows
        rows = CURSOR.fetchall()
        
        if not rows:
            print(f"No data found for store name: {store_name}")
        
        # Print each row
        for row in rows:
            print(f"""

\n{DASH} STORE DATA INSERTED {DASH}\n
Store ID       : {row[0]}
Store Name     : {row[1]}
Store Type     : {row[2]}
Visit Store    : {row[3]}
Telephone      : {row[4]}
Email          : {row[5]}
\n{DASH*3}
        """)
    time.sleep(10)
#========== end code =================

