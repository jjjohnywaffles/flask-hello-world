# Flask Application for Database Operations

## Overview
This Flask application, `app.py`, is designed to interact with a PostgreSQL database, providing routes for testing the connection, creating a table, inserting data, querying data, and dropping a table. The application demonstrates basic CRUD (Create, Read, Update, Delete) operations within a web application context.

## Requirements
- Flask
- psycopg2
- PostgreSQL database

## Installation
1. Ensure all required libraries are installed:
   ```bash
   pip install Flask psycopg2
   
2. Run the Flask application:

        python app.py
        
3. Set up the database with the provided DATABASE_URL


### Routes and Descriptions

#### `/`
- **Purpose**: A basic test route that returns a "Hello World" message.
- **Response**: `Hello World from Jonathan Hu in 3308`

#### `/db_test`
- **Purpose**: Tests the database connection to verify the application can connect to the PostgreSQL database specified by `DATABASE_URL`.
- **Response**: Returns "Database Connection Successful" if the connection is successful, or an error message if the connection fails.

#### `/db_create`
- **Purpose**: Creates a table called `Basketball` with fields for player information (first name, last name, city, team name, and jersey number).
- **SQL Command**:


          CREATE TABLE IF NOT EXISTS Basketball (
              First varchar(255),
              Last varchar(255),
              City varchar(255),
              Name varchar(255),
              Number int
          );
          
- **Response**: Returns "Basketball Table Successfully Created" if the table is created successfully, or an error message if the operation fails.

#### `/db_insert`
- **Purpose**: Inserts several sample player records into the Basketball table.
- **SQL Command**:

        INSERT INTO Basketball (First, Last, City, Name, Number) VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);

- **Response**: Returns "Basketball Table Successfully Populated" if records are successfully inserted, or an error message if the operation fails.

#### `/db_select`

- **Purpose**: Selects and displays all records from the Basketball table.
- **Response**: Returns an HTML table of all player records in the Basketball table, or an error message if the operation fails.

#### `/db_drop`

- **Purpose**: Drops the Basketball table from the database.
- **SQL Command**:

        DROP TABLE Basketball;

- **Response**: Returns "Basketball Table Successfully Dropped" if the table is dropped successfully, or an error message if the operation fails.