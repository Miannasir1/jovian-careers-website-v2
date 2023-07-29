from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':"Data Analyst",
    'location':"Gujranwala, Pakistan",
    'salary': 'Rs. 100,000'
  },
    {
    'id':2,
    'title':"Data Mining",
    'location':"Gujranwala, Pakistan",
    'salary': 'Rs. 80,000'
  },
    {
    'id':3,
    'title':"python developer",
    'location':"lahore, Pakistan",
    'salary': 'Rs. 200,000'
  },
    {
    'id':4,
    'title':"Front developer",
    'location':"sialkot, Pakistan",
   
  },
]

@app.route("/")
def hello():
  return render_template('home.html', jobs = JOBS, company_name ="MetaData")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
