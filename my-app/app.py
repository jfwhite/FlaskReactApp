from sqlalchemy import *
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relation, sessionmaker
#from flask import Flask
import os

#app = Flask(__name__)

#Base = declarative_base()

engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URL']) #'dbms://user:pwd@host/dbname'
print(engine.table_names())
#Base.metadata.create_all(engine)

#Session = sessionmaker(bind=engine)
#session = Session()

#@app.route('/')
#def hello_world():
#    return 'Hello, World!'

