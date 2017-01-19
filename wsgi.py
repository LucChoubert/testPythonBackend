import os
import pymongo
import json
from flask import Flask, request

post = {"author": "Mike", "text": "My first blog post!"}

def connectMongo():
    client = pymongo.MongoClient('mongodb://'+os.environ['MONGODB_USER']+':'+os.environ['MONGODB_PASSWORD']+'@'+os.environ['DATABASE_SERVICE_NAME']+'/'+os.environ['MONGODB_DATABASE'])
    #conn = pymongo.Connection()
    return client[os.environ['MONGODB_DATABASE']]

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World testPythonBackend!"

@application.route("/listFilms")
def listFilms():
    try:
        db = connectMongo()
        cursor = db["listFilms"].find()
        output = []
        for record in cursor:
            output.append(record)
        
        #Now turn the results into valid JSON
        print(output)
        #return str(json.dumps({'results':list(output)}))+"\n"
        return str(output)+"\n"
    except Exception as e:
        print "Error caught"
        print(e)
        return str(json.dumps({'result':'ERROR'}))+"\n"


    #return str(json.dumps({'results':list(result)},default=json_util.default))
    #return "my list of films!"

@application.route("/pushFilm", methods=["POST"])
def pushFilm():
    try:
        db = connectMongo()
        #print(request.get_data())
        db["listFilms"].insert(request.json)
        return str(json.dumps({'result':'SUCCESS'}))+"\n"
    except Exception as e:
        print "Error caught"
        print(e)
        return str(json.dumps({'result':'ERROR'}))+"\n"


@application.route("/setupSchema")
def setupSchema():
    try: 
        db = connectMongo()
        db["listFilms"].insert(post)
        
        #Now turn the results into valid JSON
        return str(json.dumps({'result':'SUCCESS'}))+"\n"
        #return str(json.dumps({'results':list(result)},default=json_util.default))
        #return "my list of films!"
    except Exception as e:
        print "Error caught"
        print(e)
        return str(json.dumps({'result':'ERROR'}))+"\n"

@application.route("/cleanSchema")
def cleanSchema():
    try: 
        db = connectMongo()
        db["listFilms"].remove()
        return str(json.dumps({'result':'SUCCESS'}))+"\n"
        #return str(json.dumps({'results':list(result)},default=json_util.default))
        #return "my list of films!"
    except Exception as e:
        print "Error caught"
        print(e)
        return str(json.dumps({'result':'ERROR'}))+"\n"

if __name__ == "__main__":
    os.environ["MONGODB_ADMIN_PASSWORD"] = "ADMINpythonBackend"
    os.environ["MONGODB_DATABASE"] = "filmsDB"
    os.environ["MONGODB_PASSWORD"] = "pythonBackend"
    os.environ["MONGODB_USER"] = "pythonBackend"
    os.environ["DATABASE_SERVICE_NAME"] = "localhost"
    application.run()
