import psycopg2
import os
#from config import app_config_dict
from flask import current_app as app


class dbMigrate:
    def __init__(self):
        self.db_name = 'iReporter_db'
        self.user_name = 'postgres'
        self.user_password = 'root'
        self.host = '127.0.0.1'
        self.port = '5432'
        self.db_connect = psycopg2.connect(
            database=self.db_name, user=self.user_name, password=self.user_password, host=self.host, port=self.port)
        self.db_connect.autocommit = True
        self.my_cursor = self.db_connect.cursor()

    #def create_tables(self):
        self.red_flag_table = "CREATE TABLE IF NOT EXISTS red_flags(\
        incident_id serial PRIMARY KEY NOT NULL,\
        comment VARCHAR (50) NOT NULL,\
        incident_type VARCHAR (10) NOT NULL,\
        incident_status VARCHAR (10) NOT NULL DEFAULT 'draft',\
        created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\
        created_by INT NOT NULL,\
        location VARCHAR (20),\
        images VARCHAR (20),\
        videos VARCHAR (20));"

        intervention_table = "CREATE TABLE IF NOT EXISTS incidents(\
        incident_id serial PRIMARY KEY,\
        comment varchar(50) NOT NULL,\
        incident_type varchar(10) NOT NULL,\
        incident_status varchar(10) NOT NUL DEFAULT 'draft',\
        created_on TIMESTAMP NOT NUL DEFAULT CURRENT_TIMESTAMP,\
        created_by int NOT NULL FOREIGN KEY REFERENCES users(user_id),\
        location varchar(20),\
        images varchar(20),\
        videos varchar(20));"

        users_table = "CREATE TABLE IF NOT EXISTS users(\
        user_id serial PRIMARY KEY,\
        firstname varchar(20) NOT NULL,\
        lastname varchar(20) NOT NULL,\
        othernames varchar(20),\
        email varchar(30) NOT NUL,\
        phoneNumber varchar(15),\
        username varchar(10) NOT NUL,\
        registered TIMESTAMP NOT NUL DEFAULT CURRENT_TIMESTAMP,\
        isAdmin boolean DEFAULT False);"

king = dbMigrate()
king.db_connect
king.my_cursor.execute(king.red_flag_table)