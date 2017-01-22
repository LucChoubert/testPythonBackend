import os
import pprint
import pymongo
import json
import flask
#from flask import request, Response

post = {"author": "Mike", "text": "My first blog post!"}

def connectMongo():
    client = pymongo.MongoClient('mongodb://'+os.environ['MONGODB_USER']+':'+os.environ['MONGODB_PASSWORD']+'@'+os.environ['DATABASE_SERVICE_NAME']+'/'+os.environ['MONGODB_DATABASE'])
    #conn = pymongo.Connection()
    return client[os.environ['MONGODB_DATABASE']]

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))+"/static"


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)


application = flask.Flask(__name__)

@application.route("/")
def hello():
    output = "Welcome in testPythonBackend\n"
    output += "===Machine & OS details===\n"
    output += pprint.pformat(os.uname())+"\n"
    output += "===ENVIRONMENT===\n"
    output += pprint.pformat(os.environ)+"\n"
    output += "===PYTHON ENVIRONMENT===\n"
    output += "flask version: "+flask.__version__+"\n"
    output += "\n"
    return output
#    return "Hello World testPythonBackend!"

@application.route("/listFilms")
#This one for bqckground compqtibility with the Node application
@application.route("/listfilms")
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
        #print(flask.request.get_data())
        #print(json.loads(flask.request.get_data()))
        db["listFilms"].insert(json.loads(flask.request.get_data()))
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

#@application.route("/static/<path:path>")
##@application.route("/static/javascripts/<path>")
##@application.route("/static/jquery/dist/<path>")
##@application.route("/static/bootstrap/dist/js/<path>")
#def distributeStaticFile(path):
#    mimetypes = {
#        ".css": "text/css",
#        ".html": "text/html",
#        ".js": "application/javascript"
#    }
#    complete_path = os.path.join(root_dir(), path)
#    extension = os.path.splitext(path)[1]
#    mimetype = mimetypes.get(extension, "text/html")
#    content = get_file(complete_path)
#    print "distributing file: "+complete_path
#    return flask.Response(content, mimetype=mimetype)



if __name__ == "__main__":
    os.environ["MONGODB_ADMIN_PASSWORD"] = "ADMINpythonBackend"
    os.environ["MONGODB_DATABASE"] = "filmsDB"
    os.environ["MONGODB_PASSWORD"] = "pythonBackend"
    os.environ["MONGODB_USER"] = "pythonBackend"
    os.environ["DATABASE_SERVICE_NAME"] = "localhost"
    application.run()
