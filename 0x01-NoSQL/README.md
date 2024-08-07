To complete the tasks described in your project, you can follow these instructions for each requirement. Below are the detailed steps for setting up and running the necessary scripts and Python functions for MongoDB:

### 0. List all databases
Write a script to list all databases in MongoDB.

```bash
echo 'show dbs' > 0-list_databases
```

Run the script:

```bash
mongo < 0-list_databases
```

### 1. Create a database
Write a script that creates or uses the database `my_db`.

```bash
echo 'use my_db' > 1-use_or_create_database
```

Run the script:

```bash
mongo < 1-use_or_create_database
```

### 2. Insert document
Write a script to insert a document with `name: "Holberton school"` into the `school` collection of `my_db`.

```bash
echo 'db.school.insert({name: "Holberton school"})' > 2-insert
```

Run the script:

```bash
mongo my_db < 2-insert
```

### 3. List all documents
Write a script to list all documents in the `school` collection of `my_db`.

```bash
echo 'db.school.find().pretty()' > 3-all
```

Run the script:

```bash
mongo my_db < 3-all
```

### 4. List documents with a specific name
Write a script to list all documents with `name="Holberton school"` in the `school` collection of `my_db`.

```bash
echo 'db.school.find({name: "Holberton school"}).pretty()' > 4-match
```

Run the script:

```bash
mongo my_db < 4-match
```

### 5. Count documents
Write a script to display the number of documents in the `school` collection of `my_db`.

```bash
echo 'db.school.countDocuments()' > 5-count
```

Run the script:

```bash
mongo my_db < 5-count
```

### 6. Update a document
Write a script to update the document with `name="Holberton school"` and add an attribute `address: "972 Mission street"`.

```bash
echo 'db.school.updateMany({name: "Holberton school"}, {$set: {address: "972 Mission street"}})' > 6-update
```

Run the script:

```bash
mongo my_db < 6-update
```

### 7. Delete documents
Write a script to delete all documents with `name="Holberton school"` in the `school` collection of `my_db`.

```bash
echo 'db.school.deleteMany({name: "Holberton school"})' > 7-delete
```

Run the script:

```bash
mongo my_db < 7-delete
```

### 8. List all documents in Python
Write a Python function to list all documents in a collection.

Create the `8-all.py` file:

```python
#!/usr/bin/env python3
def list_all(mongo_collection):
    """ Lists all documents in a collection """
    return list(mongo_collection.find())

# Ensure this script does not run when imported
if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    for doc in list_all(school_collection):
        print(doc)
```

### 9. Insert a document in Python
Write a Python function to insert a new document in a collection.

Create the `9-insert_school.py` file:

```python
#!/usr/bin/env python3
def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection """
    return mongo_collection.insert_one(kwargs).inserted_id

# Ensure this script does not run when imported
if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print(f"New school created: {new_id}")
```

### 10. Change school topics
Write a Python function to change all topics of a school document based on the name.

Create the `10-update_topics.py` file:

```python
#!/usr/bin/env python3
def update_topics(mongo_collection, name, topics):
    """ Updates the topics of a school document """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

# Ensure this script does not run when imported
if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])
    for doc in school_collection.find():
        print(doc)
```

### 11. List schools by topic
Write a Python function to return the list of schools having a specific topic.

Create the `11-schools_by_topic.py` file:

```python
#!/usr/bin/env python3
def schools_by_topic(mongo_collection, topic):
    """ Returns the list of schools having a specific topic """
    return list(mongo_collection.find({"topics": topic}))

# Ensure this script does not run when imported
if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print(school)
```

### 12. Log stats
Write a Python script to provide stats about Nginx logs stored in MongoDB.

Create the `12-log_stats.py` file:

```python
#!/usr/bin/env python3
from pymongo import MongoClient

def log_stats():
    """ Provides stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
```

To run these scripts and functions, ensure you have MongoDB and PyMongo installed and properly set up on your system. Follow the provided installation commands if necessary.
