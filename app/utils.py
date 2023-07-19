import time
import requests
import os
import json
import logging
from datetime import datetime, date
import pandas as pd
from sqlalchemy import create_engine

username = "user"
password = "pass"
host = "postgres"
port = "5432"
database = "user"


def read_sql(sql_path):
    with open(f"/workdir/app/sql/{sql_path}") as f:
        query = " ".join(f.readlines()).replace("\n", "").replace("\t", "")
        f.close()
    return query


def send_query(query):
    logging.info(f"Start sending sql query")
    engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")
    result = pd.read_sql(query, engine)
    logging.info(f"Collect result of sql query")
    return str(result)