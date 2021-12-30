#https://flask.palletsprojects.com/en/2.0.x/patterns/sqlalchemy/

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from sqlalchemy.sql import expression, functions
from sqlalchemy import types
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto-mpg.db'
db = SQLAlchemy(app)


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
    
print(get_column_names())

if check_if_ID_col_exists() == False: #if we haven't created an ID column yet, do
    #create ID Column
    #by combining carname + modelyear
    #should be a unique identifier
    with engine.connect() as con:
        result = con.execute("SELECT (carname||\" \"||modelyear) AS nameyearID FROM cars") 
        print(result)
    pass


car_put_args = reqparse.RequestParser()
car_put_args.add_argument("nameyearID",type=str, help="Name of video", required=False)
car_put_args.add_argument("mpg",type=float)
car_put_args.add_argument("cylinders",type=int, help="Likes on the video")
car_put_args.add_argument("displacement",type=int)
car_put_args.add_argument("weight",type=int, help="Likes on the video")
car_put_args.add_argument("acceleration",type=float)
car_put_args.add_argument("modelyear",type=int, help="Likes on the video")
car_put_args.add_argument("origin",type=int)
car_put_args.add_argument("carname",type=str, help="Likes on the video")

resource_fields = {
    'nameyearID': fields.String,
    'mpg': fields.Float,
    'cylinders': fields.Integer,
    'displacement': fields.Integer,
    'weight': fields.Integer,
    'acceleration': fields.Float,
    'modelyear': fields.Integer,
    'origin': fields.Integer,
    'carname': fields.String,
}



## 'mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'modelyear', 'origin', 'carname'
class CarModel(db.Model):
    nameyearID = db.Column(db.String(250), primary_key=True)
    mpg = db.Column(db.Float, nullable=False)
    cylinders = db.Column(db.Integer, nullable=False)
    displacement = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    acceleration = db.Column(db.Float, nullable=False)
    modelyear = db.Column(db.Integer, nullable=False)
    origin = db.Column(db.Integer, nullable=False)
    carname = db.Column(db.String(250), nullable=False)
    
    def __repr(self):
        return f"Video(name={name}, views={views}, likes={likes}"

class Car(Resource):
    @marshal_with(resource_fields) #serialize return values with resource_fields
    def get(self, nameyearID):
        result = CarModel.query.filter_by(id=nameyearID).first() #get first video_id
        if not result:
            abort(404, message="could not ind video with that id")
        return result
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=nameyearID).first()
        if result:
            abort(409, message="Video id taken...")
        video = VideoModel(id=video_id, name=args["name"], views=args["views"], likes=args["likes"])
        db.session.add(video)
        db.session.commit()
        return video, 201

    def delete(self, video_id):
        pass
    
    def patch(self, video_id):
        args = video_put_args.parse_args()
        #query database, getobject, modify object & commit

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

#column_names = db.__table__.columns.keys()  
#print(column_names)
#db.session.commit() 

#column_names = conn.execute(query).keys()


#Combining with SQLAlchemy
# ^^^ link: https://stackoverflow.com/questions/17265848/concatenating-columns-at-query-level-in-sqlalchemy
#functions.concat(
#    expressions.cast(table1.col2, types.Unicode), table2.col2)



'''
class VideoModel(db.Model):
    car_name = db.Column((db.String(250), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
'''

if __name__ == "__main__":
    app.run(debug=True)
