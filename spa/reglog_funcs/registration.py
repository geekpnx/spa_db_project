import bcrypt
import re
import os
import time
import getpass

from spa.deco.spa_db_banner import spa_banner
from spa.connection.spa_db_connect import spa_db_connection
from spa.connection.spa_db_check_conn import spa_db_check_connection

CONNECT, CURSOR = spa_db_connection()
DB_CHECK = spa_db_check_connection()
BANNER = spa_banner()
DASH = 10*'═'
SIGN = f"\n{DASH} REGISTRATION {DASH}\n"

def goback(back_to_front):
    input("\n ↩️ Press Enter to return to Insert Data menu... or CONTROL+C to exit program")
    back_to_front()

PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9_]{3,30}$')


def register_user():
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        username = input("Create username: ")
        query_un = """
        SELECT username FROM users WHERE username = %s;
        """
        CURSOR.execute(query_un,(username,))
        if CURSOR.fetchone():
            print("\n** Username already exists **.\nPlease choose a different username.\n")
        elif not USERNAME_REGEX.match(username):
            print(f"\n❌ Invalid {username}!\n\nPlease follow the criteria:\n- Lower case [a-z]\n- Upper case [A-Z]\n- Numbers [e.i 0-9]\n- Underscore ['_']\n")
        else:
            break
        
    while True:
        password = getpass.getpass("Create password: ")
        if not PASSWORD_REGEX.match(password):
            print("\n❌ Password does not meet the requirements\n\nPlease follow the criteria:\n- Between 6 to 20 charecters in length\n- At least one upper case [A-Z]\n- At least one number [e.i 0-9]\n- At least one special Characters\n")
        else:
            break
    while True:  
        email = input("Enter email: ")
        query_mail = """
        SELECT email FROM users WHERE email = %s;
        """
        CURSOR.execute(query_mail,(email,))
        if not EMAIL_REGEX.match(email):
            print("\n❌ Email is not valid")
        else:
            break
    
            

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    query = """
    INSERT INTO users(
        username, 
        password_hash, 
        email
    ) 
    VALUES (%s, %s, %s)
    RETURNING *;
    """
  

    CURSOR.execute(query,(username, hashed_password, email))
    CONNECT.commit()
    print(f"\n ✅ User {username} registered successfully")
    time.sleep(3)


