#https://flask.palletsprojects.com/en/2.0.x/patterns/sqlalchemy/

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from sqlalchemy.sql import expression, functions
from sqlalchemy import types
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table

app = Flask(__name__)
api = Api(app)

engine = create_engine('sqlite:///auto-mpg.db')
metadata = MetaData(bind=engine)

def get_column_names(ENGINE=engine):
    '''
    Description:
    Used to collect a list of all column names
    with the database engine
    
    Parameters:
    * Engine ~ A SQLAlchemy engine connected to sqlite database
    * * * * Default: database engine in global scope
    
    Returns:
    a python list of each column in the database
    '''
    with ENGINE.connect() as con: #creating a new connection to the database
        #Simply checking if an ID column exists in the database or if we need to create one
        column_names = [] #Every column
        result = con.execute("PRAGMA table_info('cars')") #returns iterable of tuples
        for row in result:
        print(row)
            column_names.append(row[1])
    return column_names

def check_if_ID_col_exists(COL_NAME="ID", COLUMN_NAMES=get_column_names()):
    '''
    Description:
    Checks if the current database includes an column with 
    the name COL_NAME. Returns True if ID column exists, 
    otherwise it returns False.
    
    Parameters:
    * COLUMN_NAMES ~ a python list of each column in the database
    * * * * Default: Creates a list with get_column_names method
    * COL_NAME ~ a python string
    * * * * Default: "ID"
    
    Returns:
    a bool either True or False. True if the column does exist,
    False if it does not exist.
    '''
    if COL_NAME in COLUMN_NAMES:
        return True
    else:
        return False
    
if check_if_ID_col_exists == True:
    #create ID Column
    
    
#conn = engine.connect()
#column_names = conn.execute(query).keys()
#column_names = engine.execute('SELECT * FROM cars').all()

#db = SQLAlchemy(app)
#db.create_all() #only run once

#Need to check if unique identifier column is in database, if not 
#Use this mtheod: https://stackoverflow.com/questions/5385142/how-to-combine-two-columns-in-sqlite-in-python
#Car names are unique if model year is included

#Getting Column names
# ^^^ link: https://stackoverflow.com/questions/6455560/how-to-get-column-names-from-sqlalchemy-result-declarative-syntax

'''
with Session(engine) as session: # https://docs.sqlalchemy.org/en/14/orm/session_basics.html#basics-of-using-a-session
    session.begin()
    try:
        session.add(some_object)
        session.add(some_other_object)
    except:
        session.rollback()
        raise
    else:
        session.commit()
'''

#engine = create_engine('sqlite:///auto-mpg')

column_names = db.__table__.columns.keys()  
print(column_names)
db.session.commit() 

#column_names = conn.execute(query).keys()


#Combining with SQLAlchemy
# ^^^ link: https://stackoverflow.com/questions/17265848/concatenating-columns-at-query-level-in-sqlalchemy
functions.concat(
    expressions.cast(table1.col2, types.Unicode), table2.col2)



'''
class VideoModel(db.Model):
    car_name = db.Column((db.String(250), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
'''

if __name__ == "__main__":
    app.run(debug=True)
