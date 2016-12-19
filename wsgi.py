import os
import pymongo
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World testPythonBackend!"

@application.route("/listFilms")
def listFilms():
	#setup the connection
        conn = pymongo.Connection(os.environ['OPENSHIFT_NOSQL_DB_URL'])
        db = conn.parks
 
        #query the DB for all the parkpoints
        result = db.parkpoints.find()
 
	#Now turn the results into valid JSON
        return str(json.dumps({'results':list(result)},default=json_util.default))
    	#return "my list of films!"


if __name__ == "__main__":
    application.run()
