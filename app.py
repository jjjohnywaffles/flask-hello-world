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

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://jjjohnywaffles_user:EK7LeBnEN9tqa9jJwrWt3cOnvRRWG5LD@dpg-cshblsd6l47c73advt40-a/jjjohnywaffles")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://render_example_ocz5_user:password@hostname:port/database_name")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number) Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"