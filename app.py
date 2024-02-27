from flask import Flask, render_template, jsonify
from database import load_jobs_from_db


app = Flask(__name__)

# JOBS = [
#   {
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Bengaluru, India',
#     'salary': 'Rs. 10,00,000'
#   },
#   {
#     'id': 2,
#     'title': 'Data Scientist',
#     'location': 'Delhi, India',
#     'salary': 'Rs. 15,00,000'
#   },
#   {
#     'id': 3,
#     'title': 'Frontend Engineer',
#     'location': 'Remote',
#     'salary': 'Rs. 12,00,000'
#   },
#   {
#     'id': 4,
#     'title': 'Backend Engineer',
#     'location': 'San Francisco, USA',
#     'salary': '$150,000'
#   }
# ]


@app.route('/')
def hello_jovian():
  jobs = load_jobs_from_db()
  return render_template("base.html", 
                          jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080,   debug=True)