import psycopg2
import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()
cur.execute("""
             CREATE TABLE IF NOT EXISTS userdetail(
                   id  serial,
                   name varchar,
                   username varchar UNIQUE,
                   emailid varchar UNIQUE,
                   mbnos varchar UNIQUE,
                   salt varchar,
                   hashed_password varchar,
                   PRIMARY KEY(id)
                );
        """)
conn.commit()