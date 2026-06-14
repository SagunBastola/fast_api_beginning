import sqlite3

from fastapi import FastAPI
conn=sqlite3.connect("user.db")
cursor=conn.cursor()
cursor.execute("""create table if not exists user
               (id INTEGER PRIMARY KEY,
               user_name TEXT,
               completed TEXT )
               """)
conn.commit()

app=FastAPI()

@app.get("/")
def root():
    return {
        "message":"sqlite connected fine"
    }