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
SIGN = f"\n{DASH} LOGIN {DASH}\n"

def goback(back_to_front):
    # input("\n ↩️ Press Enter to got to the Main Menu.")
    back_to_front()

PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9_]{3,30}$')


def login_user(back_to_front):
    os.system('clear')
    print(f"{BANNER}\n{DB_CHECK}\n")
    print(SIGN)
    while True:
        os.system('clear')
        print(f"{BANNER}\n{DB_CHECK}\n")
        print(SIGN)
        username = input("Enter username: ")
        query_un = """
        SELECT username FROM users WHERE username = %s;
        """
        CURSOR.execute(query_un,(username,))
        if not CURSOR.fetchall():
            print(f"\n❌ Username '{username}' does not exist.\n")
            time.sleep(3)
        elif not USERNAME_REGEX.match(username):
            print(f"\n❌ Username '{username}' is invalid!")
            time.sleep(3)
        else:
            break
        
    while True:
        password = getpass.getpass("Enter password: ")
        query_pwd = """
        SELECT user_id, password_hash FROM users WHERE username = %s;
        """
        CURSOR.execute(query_pwd,(username,))
        user = CURSOR.fetchone()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
            user_id = user[0]
            query_insert = """
            INSERT INTO user_sessions (
                user_id, 
                status) 
            VALUES (%s, %s)
            """
            CURSOR.execute(query_insert,(user_id, 'logged_in'))
            CONNECT.commit()
            print(f"\n Hello 👤 {username}, you are logged in successfuly")
            time.sleep(5)
            goback(back_to_front)

        else:
            print(f"\n❌ Password is invalid!")
            time.sleep(3)
            return login_user(back_to_front)


if __name__ == "__main__":
    login_user()


    
            



