import psycopg2
import os
#from config import app_config_dict
from flask import current_app as app
from psycopg2.extras import RealDictCursor


class DBmigrate:
    def __init__(self):
        self.db_name = 'iReporter_db'
        self.user_name = 'postgres'
        self.user_password = 'root'
        self.host = '127.0.0.1'
        self.port = '5432'
        self.db_connect = psycopg2.connect(
            database=self.db_name, user=self.user_name, password=self.user_password, host=self.host, port=self.port)
        self.db_connect.autocommit = True
        self.my_cursor = self.db_connect.cursor(cursor_factory = RealDictCursor)
        #self.con_close = self.db_connect.close()

    def create_tables(self):
        red_flag_table = "CREATE TABLE IF NOT EXISTS red_flags(\
        incident_id serial PRIMARY KEY NOT NULL,\
        comment VARCHAR (50) NOT NULL,\
        incident_type VARCHAR (15) DEFAULT 'red-flag',\
        incident_status VARCHAR (10) NOT NULL DEFAULT 'draft',\
        created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\
        created_by INT NOT NULL,\
        location VARCHAR (20),\
        images VARCHAR (20),\
        videos VARCHAR (20));"

        intervention_table = "CREATE TABLE IF NOT EXISTS incidents(\
        incident_id serial PRIMARY KEY NOT NULL,\
        comment VARCHAR (50) NOT NULL,\
        incident_type VARCHAR (15) DEFAULT 'intervention',\
        incident_status VARCHAR (10) NOT NULL DEFAULT 'draft',\
        created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\
        created_by INT NOT NULL,\
        location VARCHAR (20),\
        images VARCHAR (20),\
        videos VARCHAR (20));"

        users_table = "CREATE TABLE IF NOT EXISTS users(\
        user_id serial PRIMARY KEY,\
        firstname VARCHAR(20) NOT NULL,\
        lastname VARCHAR(20) NOT NULL,\
        othernames VARCHAR(20),\
        email VARCHAR(30) NOT NULL,\
        phoneNumber VARCHAR(15),\
        username VARCHAR(10) NOT NULL,\
        password TEXT NOT NULL,\
        registered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\
        isAdmin boolean DEFAULT False);"

        self.db_connect
        self.my_cursor.execute(users_table)
        self.my_cursor.execute(red_flag_table)
        self.my_cursor.execute(intervention_table)

    def drop_table(self,table_name):
        dropper = "DROP TABLE IF EXISTS {}".format(table_name)
        self.my_cursor.execute(dropper)

    

