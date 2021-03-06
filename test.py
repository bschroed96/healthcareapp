import pymongo
import ssl
import os

user = os.environ['USER']
pwd = os.environ['PWD']
endpoint = os.environ['END']

if __name__ == '__main__':
    client = pymongo.MongoClient(
        "mongodb+srv://" + user + ":" + pwd + endpoint,
        ssl_cert_reqs=ssl.CERT_NONE
    )
    db = client.test

    posts = db.posts

    post_data = {
        'title': 'python and mongoDB',
        'content': 'pymongo is fun, you guys',
        'author': 'Scott'
    }
    result = posts.insert_one(post_data)
    print('One post: {0}'.format(result.inserted_id))