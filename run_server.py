#data comes from https://www.kaggle.com/austinreese/craigslist-carstrucks-data

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from sqlalchemy.sql import expression, functions
from sqlalchemy import types
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

app = Flask(__name__)
api = Api(app)
db_URL = 'sqlite:///auto-mpg.db'
db = SQLAlchemy(app)
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

column_names = conn.execute(query).keys()


#Combining with SQLAlchemy
# ^^^ link: https://stackoverflow.com/questions/17265848/concatenating-columns-at-query-level-in-sqlalchemy
functions.concat(
    expressions.cast(table1.col2, types.Unicode), table2.col2)



'''
class VideoModel(db.Model):
    car_name = db.Column((db.String(250), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
'''
