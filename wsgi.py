import os
import pymongo
import json
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World testPythonBackend!"

@application.route("/listFilms")
def listFilms():
	#setup the connection
	client = pymongo.MongoClient('mongodb://'+os.environ['MONGODB_USER']+':'+os.environ['MONGODB_PASSWORD']+'@'+os.environ['DATABASE_SERVICE_NAME']+'/'+os.environ['MONGODB_DATABASE'])
        #conn = pymongo.Connection()
        db = client[os.environ['MONGODB_DATABASE']]
 	result = db.collection_names()

        #query the DB for all the parkpoints
        #result = db.parkpoints.find()
 
	#Now turn the results into valid JSON
        return str(json.dumps({'results':list(result)}))
        #return str(json.dumps({'results':list(result)},default=json_util.default))
    	#return "my list of films!"


if __name__ == "__main__":
    application.run()
