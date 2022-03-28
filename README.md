# Reddit Recovery Dashboard
 
Use this video to set up postgres. https://www.youtube.com/watch?v=7EeAZx78P2U

These are the commands to run from a python terminal. 

from dashboard import db
db.create_all()

Comment and post models from monty are commented out for now. You only need to make the table for "users" right now.

Exact syntax used to create users table in postgres terminal 

CREATE TABLE users(id SERIAL PRIMARY KEY,username VARCHAR(25) UNIQUE NOT NULL);
