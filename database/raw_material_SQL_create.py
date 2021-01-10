import pyodbc
import pandas as pd
import json

with open('raw_mat_config.json') as config:
    config_data = json.load(config)


# Create database
def create_db(sql_command):
    conn = pyodbc.connect('''
                            driver={SQL Server}; 
                            server=A909US107;
                            trusted_connection=True;
                        ''') 

    conn.autocommit = True

    cursor = conn.cursor()

    cursor.execute(sql_command)

create_table = "CREATE DATABASE [RawMat_beta]"

create_db(create_table)



# Create tables
tables = {

}

for table in tables:
    #cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
    sql_command = "", (table)
    create_db(sql_command)
