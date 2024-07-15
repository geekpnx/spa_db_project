import psycopg
import environs
from spa.utils import ROOT_DIR
#---- SPA DB connection ----

env = environs.Env()
env.read_env(str(ROOT_DIR / '.env'))

def spa_db_connection():

    CONN= psycopg.connect(
        dbname = env.str("DB_NAME"),
        user = env.str("DB_USER"),
        password = env.str("DB_PWD"), 
        port = 5432,
        host = env.str("DB_HOST")
    )

    CUR = CONN.cursor()
    return CONN, CUR

