import psycopg2
from flask import Flask
app = Flask(__name__)

DATABASE_URL = "postgresql://jjjohnywaffles_user:EK7LeBnEN9tqa9jJwrWt3cOnvRRWG5LD@dpg-cshblsd6l47c73advt40-a/jjjohnywaffles"

@app.route('/')
def hello_world():
    return 'Hello World from Jonathan Hu in 3308'

@app.route('/db_test')
def db_test():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        return "Database Connection Successful"
    except OperationalError as e:
        return f"Database Connection Failed: {e}"

@app.route('/db_create')
def creating():
    try:
        conn = psycopg2.connect(DATABASE_URL)
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
        return "Basketball Table Successfully Created"
    except (OperationalError, DatabaseError) as e:
        return f"Error Creating Table: {e}"
    finally:
        if 'conn' in locals() and conn:
            conn.close()

@app.route('/db_insert')
def inserting():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number) VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
        conn.commit()
        return "Basketball Table Successfully Populated"
    except (OperationalError, DatabaseError) as e:
        return f"Error Inserting Data: {e}"
    finally:
        if 'conn' in locals() and conn:
            conn.close()

@app.route('/db_select')
def selecting():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute('''
            SELECT * FROM Basketball;
        ''')
        records = cur.fetchall()
        
        response_string = "<table>"
        for player in records:
            response_string += "<tr>"
            for info in player:
                response_string += "<td>{}</td>".format(info)
            response_string += "</tr>"
        response_string += "</table>"
        
        return response_string
    except (OperationalError, DatabaseError) as e:
        return f"Error Selecting Data: {e}"
    finally:
        if 'conn' in locals() and conn:
            conn.close()

@app.route('/db_drop')
def dropping():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute('''
            DROP TABLE Basketball;
        ''')
        conn.commit()
        return "Basketball Table Successfully Dropped"
    except (OperationalError, DatabaseError) as e:
        return f"Error Dropping Table: {e}"
    finally:
        if 'conn' in locals() and conn:
            conn.close()