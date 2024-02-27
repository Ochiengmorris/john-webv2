import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, text
import os

db_conection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_conection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()
    jobs = []
    for row in result_all:
      jobs.append(row._asdict())

    return jobs