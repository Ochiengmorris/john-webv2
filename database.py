import sqlalchemy
from sqlalchemy import create_engine, text
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

# new = load_jobs_from_db()
# print(new)

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from jobs where id = :val"), {'val': id}
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()

def add_applications_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, fullName, email, linkedin_url, resume_url, work_experience, education) VALUES (:job_id, :fullName, :email, :linkedin_url, :resume_url, :work_experience, :education)")
    conn.execute(query, {
      'job_id': job_id, 
      'fullName': data['fullName'], 
      'email': data['email'], 
      'linkedin_url': data['linkedin_url'], 
      'resume_url': data['resume_url'], 
      'work_experience': data['work_experience'], 
      'education': data['education']
    })