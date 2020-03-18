#coding=utf-8
import json

from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="192.168.1.109")

# result = es.indices.create(index='news', ignore=400)
#
# print(result)


mapping = {
    "_doc": {

        'properties':{

             'title':  {

                'type': 'text',

                'analyzer': 'ik_max_word',

                'search_analyzer': 'ik_max_word'

            }

    }
    }
}

# es.indices.delete(index='news', ignore=[400, 404])

people={
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "type": {"type": "keyword"},
      "name": {"type": "text"},
      "country": {"type": "keyword"},
      "age": {"type": "integer"},
      "date": {
        "type": "date",
        "format": "yyyy-MM-dd HH:mm:ss || yyyy-MM-dd || epoch_millis"
      }
    }
  }
}

# result=es.indices.create(index="people", body=people,ignore=400)
# print(result)

# result=es.indices.delete(index='_na_', ignore=[400, 404])
# print(result)

# result = es.indices.put_mapping(index='news', doc_type='politics', body=mapping)

data = {
  "type": "man",
  "name": "AutoZereao",
  "country": "China",
  "age": "23",
  "date": "1995-11-27 12:25:35"
}

data1={
  "type": "man",
  "name": "Zereao",
  "country": "China",
  "age": "23",
  "date": "1995-11-27"
}
datas=[
{
  "type": "woman",
  "name": "Maryb",
  "country": "China",
  "age": "24",
  "date": "1995-12-27"
},
{
  "type": "woman",
  "name": "Mary",
  "country": "China",
  "age": "21",
  "date": "1995-11-22"
},
{
  "type": "woman",
  "name": "Marya",
  "country": "China",
  "age": "25",
  "date": "1995-11-21"
}

]
# result=es.create(index="people",id=2, body=data1)
#
# print(result)
# i=3

