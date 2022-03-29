# Reddit Recovery Dashboard
 
Use this video to set up postgres. https://www.youtube.com/watch?v=7EeAZx78P2U

In Postgres terminal/GUI: The URI and credentials need to be the same!

EITHER:
- set postgres user password to admin
- create database "first"
- create table (CREATE TABLE users(id SERIAL PRIMARY KEY,username VARCHAR(25) UNIQUE NOT NULL);)

OR: 
Change this line in init_py:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/first'
to
'postgressql://[username]:[password]@localhost/[databasename]'

These are the commands to run from a python terminal. 

from dashboard import db
db.create_all()

Comment and post models from monty are commented out for now. You only need to make the table for "users" right now.


