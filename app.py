from fastapi import FastAPI
from utils import read_sql, send_query

app = FastAPI()

@app.get("/check")
def check():
    return "API is ready"

@app.get("/get_tables")
def get_tables():
    query = read_sql("get_tables.sql")
    response = send_query(query)
    return response

@app.get("/try_select")
def select():
    query = read_sql("select_1.sql")
    response = send_query(query)
    return response