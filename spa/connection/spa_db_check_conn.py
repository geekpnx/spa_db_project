from spa.connection.spa_db_connect import spa_db_connection
from psycopg import OperationalError

CONNECT, CURSOR = spa_db_connection()


def spa_db_check_connection():
    try: 
        CURSOR.execute("SELECT 1")
        CURSOR.fetchone()

        return "🟢 DB Online & Connected\n"


    except OperationalError as e:
        return print("\n🔴 Database Offline & Disconnected"), print(f"Error{e}")



