from lxml import etree
from simplejson import JSONEncoder
import requests
import json
import glob

def dumpLeaf(leaf,n=0):
    for child in leaf:
            if len(child) is 0 and child.text is not None:
                print(n*" "+child.tag+":"+child.text)
            else:
                if len(child) > 0:
                    print(n*" "+child.tag)
                    dumpLeaf(child,n+1)

def encodeLeaf(leaf,structure):
    for child in leaf:
        if len(child) is 0 and child.text is not None:
            if child.tag in structure.keys():
                out = structure[child.tag]
                #print("Tag available:"+child.tag,structure[child.tag])
                if isinstance(out, list) is not True:
                    new_list = []
                    new_list.append(out)
                    structure[child.tag]=new_list
                structure[child.tag].append(child.text)
                #print("Tag updated:"+child.tag,structure[child.tag])
            else:
                structure[child.tag]=child.text
        else:
            if len(child) > 0:
                new_structure = {}
                encodeLeaf(child,new_structure)
                if child.tag in structure.keys():
                    out = structure[child.tag]
                    if isinstance(out, list) is not True:
                        new_list = []
                        new_list.append(out)
                        structure[child.tag]=new_list
                    structure[child.tag].append(new_structure)
                else:                
                    structure[child.tag]=new_structure

def convert_MediaElchNFO_to_JSON(filename):
    tree = etree.parse(filename)
    root = tree.getroot()
    #dumpLeaf(root)
    movie = {}
    encodeLeaf(root,movie)
    return JSONEncoder().encode(movie)



if __name__ == '__main__':
    #url = 'http://testpythonbackend-testpython.44fs.preview.openshiftapps.com'
    url = 'http://localhost:5000'
    action = 'pushFilm'
    #for f in glob.glob('/home/luc/Python/testPythonBackend/*.nfo'):
    for f in glob.glob('./*.nfo'):
        movie_json = convert_MediaElchNFO_to_JSON(f)
        #print(movie_json)
        response = requests.post(url+'/'+action, movie_json)
        print("Importing "+json.loads(movie_json)['title']+" ---> "+response.json()['result'])
    