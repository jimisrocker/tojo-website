from flask import Flask
from flask_mongoengine import MongoEngine
from os import path
import os
from dotenv import load_dotenv, find_dotenv


BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(find_dotenv())
  
db=MongoEngine()
DB_NAME='mongodb'
#initialize app
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']= os.getenv('SECRET_KEY')
    app.config['MONGODB_SETTINGS']={
        'db':'tojocluster',
        'host':'mongodb+srv://'+os.getenv('MONGO_USER')+':'+os.getenv('MONGO_PASS')+'@tojocluster.aniph.mongodb.net/tojocluster?retryWrites=true&w=majority'
    }

    #mongo database initialization
    
    db.init_app(app)


    #load views and configspip
    from .views import views
    app.register_blueprint(views,url_prefix='/')
    
    #from .models import Business
    #create_database(app)

    return app


def create_database(app):
    if not path.exists('app/'+DB_NAME):
        db.create_all(app=app)
        print('created database')
    
    