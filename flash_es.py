import flask
import rawes
import json
from flask import Flask

query = "python"

es = rawes.Elastic('localhost:9200')
response = es.get('dns/nyc/_search', data={
    "query":{
        "bool":{
            "must":[{
                "wildcard":{
                    "answer":query
                    }}],
                "must_not":[],
                "should":[]}},
        "from":0,
        "size":50,
        "sort":[],
        "facets":{}
        })


back = response['hits']['hits'][0]['_source'].values()
app = Flask(__name__)

@app.route('/')

def hello_world():
    return back[3]


if __name__ == '__main__':    
    app.run()
