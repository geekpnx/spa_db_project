import subprocess
from connection.spa_db_connect import spa_db_connection
from psycopg2 import OperationalError

CONNECT, CURSOR = spa_db_connection()
CMD = "pg_ctl -D spa_clstr_7777 stop"

def spa_db_close_connection():
    try: 
        CURSOR.close
        CONNECT.close()
        close_db = subprocess.run(CMD, shell=True, text=True)
        return close_db, print("\n\nDatabase is offline and disconnected 🔴")


    except OperationalError as e:
       return print(f"Error{e}")
