#oc login 10.2.2.2:8443 -u=admin -p=admin
oc login --token=FtLOzpMHmbo5Gbx86NZJfQaOkId9WTgK-o9Z17GcLBw --server=https://api.preview.openshift.com

oc delete dc/mongodb
oc delete service/mongodb

oc delete all -l app=testpythonbackend
oc delete project testpython

oc new-project testpython --description="testpython" --display-name="testpython"
oc project testpython

oc new-app openshift/python:2.7~https://github.com/LucChoubert/testPythonBackend.git
#oc new-app --strategy=source https://github.com/LucChoubert/testPythonBackend.git
#oc new-app --image-stream=openshift/python:latest --code=https://github.com/LucChoubert/testPythonBackend.git

oc new-app openshift/mongodb:3.2

oc env dc testpythonbackend mongodb DATABASE_SERVICE_NAME=mongodb MONGODB_USER=pythonBackend MONGODB_PASSWORD=pythonBackend MONGODB_DATABASE=filmsDB MONGODB_ADMIN_PASSWORD=ADMINpythonBackend

oc expose service/testpythonbackend

oc get bc
oc get dc
oc get pods
oc get services
oc get routes



#Monitor logs Build
#oc logs -f bc/testpythonbackend
#Monitor logs Deployment
#oc logs -f dc/testpythonbackend

oc status


#git commit; git push
oc start-build bc/testpythonbackend


#curl http://testpythonbackend-testpython.44fs.preview.openshiftapps.com/listFilms




