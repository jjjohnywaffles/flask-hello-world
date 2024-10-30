import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Jonathan Hu in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://jjjohnywaffles_user:EK7LeBnEN9tqa9jJwrWt3cOnvRRWG5LD@dpg-cshblsd6l47c73advt40-a/jjjohnywaffles")
    conn.close()
    return "Database Connection Successful"
