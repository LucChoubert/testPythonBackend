#To test en local
# cd ~/Python/testPythonBackend
#
# python wsgi.py 

curl  http://localhost:5000
curl  http://localhost:5000/listFilms
#curl  http://localhost:5000/cleanSchema
#curl  http://localhost:5000/setupSchema
#curl -H "Content-Type: applicatio#/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:5000/pushFilm


#curl http://testpythonbackend-testpython.44fs.preview.openshiftapps.com/listFilms

