import json
import os
from random import randrange

def create_db(database_name):
    os.makedirs(database_name, exist_ok=True)
    return print(f"Database created {database_name}")

create_db('DB')

def create_collection(database, collection):
    file_name = os.path.join(database, collection)

    if not os.path.exists(file_name):
        with open (file_name, 'w', encoding='utf8') as f:
            json.dump([], f)

    return file_name

collection = create_collection("DB", "posts.json")

def save(data):
    entry = data
    file_name = collection
    
    if os.path.exists(file_name):
        with open (file_name, 'r', encoding='utf8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
        
        # add the data in the list
        data.append(entry)
        
        # save the list
        with open (file_name, 'w', encoding='utf8') as f:
            json.dump(data, f)
    else:
        print("File not found")

data = {"id": randrange(0, 1000000), "Panda": "Coder"}
save(data)

def load():
    if os.path.exists(collection):
        with open (collection, 'r', encoding='utf8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        print("Collection not found:" + str(collection))
    return data

# print(load())

def update(id, data):
    '''update the file by id and updating every thing'''
    pass

# data = {"id": randrange(0, 100000),"savage": "presentation"}
# update(1, data)