from pymongo import MongoClient


URI = f'mongodb+srv://yoon:yoon123@cluster0.hxzch.mongodb.net/Project0?retryWrites=true&w=majority'

client = MongoClient(URI)

print(client)

DATABASE = 'price'

db = client[DATABASE]

coll = db['price']

import json

with open('kc_house_data.json') as f :
    coll.insert_many(json.load(f))
