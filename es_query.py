import rawes
es = rawes.Elastic('localhost:9200')
query = "python"
es.get('dns/nyc/_search', data={
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


query = "*google*"

es.get('dns/nyc/_search', data={
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
