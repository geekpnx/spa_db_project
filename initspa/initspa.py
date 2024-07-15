import os
import subprocess


def run_psql_command_user(command):
    print("\nCreate 'spa_admin' as the user.\nPlease enter the password 'postgres', when it prompts you.")
    result = subprocess.run(['psql', '-h','localhost','-U','postgres', '-d','postgres', '-c', command], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")

# Create a PostgreSQL user
create_user_command = "CREATE ROLE spa_admin WITH LOGIN SUPERUSER CREATEDB CREATEROLE PASSWORD 'password';"
run_psql_command_user(create_user_command)

# Create a database
def run_psql_command_db(command):
    print("\nCreate database 'spa_db' as the user 'spa_admin'.\nPlease enter the password 'password', when it prompts you.")
    result = subprocess.run(['psql', '-h','localhost','-U','spa_admin', '-d','postgres', '-c', command], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")

create_db_command = "CREATE DATABASE spa_db;"
run_psql_command_db(create_db_command)

# Create tables
def run_psql_command_tbl(command_file):
    print("\nRequire tables have been created into the  database 'spa_db'")
    os.environ['PGPASSWORD'] = 'password'  # Replace 'your_password' with the actual password

    # Run the psql command
    result = subprocess.run(
        ['psql', '-h', 'localhost', '-U', 'spa_admin', '-d', 'spa_db', '-f', command_file],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")

# Construct the path to the SQL file relative to the current working directory
current_directory = os.getcwd()
sql_file_name = "create_tables_on_SPA.sql"
relative_path = os.path.join(current_directory, "sql_queries", sql_file_name)

# Execute the command
run_psql_command_tbl(relative_path)


# Insert Data
def run_psql_command_ins(command_file):
    print("\nExample data inserted into the database 'spa_db'")
    # Set the password for the PostgreSQL user
    os.environ['PGPASSWORD'] = 'password'  # Replace 'your_password' with the actual password

    # Run the psql command
    result = subprocess.run(
        ['psql', '-h', 'localhost', '-U', 'spa_admin', '-d', 'spa_db', '-f', command_file],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")

# Construct the path to the SQL file relative to the current working directory
current_directory = os.getcwd()
sql_file_name = "insert_data_to_SPA.sql"
relative_path = os.path.join(current_directory, "sql_queries", sql_file_name)

# Execute the command
run_psql_command_ins(relative_path)
# login to spa_db
# def run_psql_login_spadb():
#     os.environ['PGPASSWORD'] = 'password'  # Replace 'your_password' with the actual password
#     result = subprocess.run(['psql', '-U', 'spa_admin', '-d', 'spa_db'])
#     if result.returncode != 0:
#         print(f"Error: {result.stderr}")
#     else:
#         print("Opened interactive psql session")
# 
# run_psql_login_spadb()
