import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, text

engine = create_engine("mysql+pymysql://uuw9tx5zc8ourru5:1No9xyimyKUi5X89BPpG@byvfcqdtynk11snvfbgr-mysql.services.clever-cloud.com/byvfcqdtynk11snvfbgr?charset=utf8mb4")

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()
    jobs = []
    for row in result_all:
      jobs.append(row._asdict())

    return jobs