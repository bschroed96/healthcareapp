import pymongo
import ssl
import os
import pprint


class Post:
    pass


class Get:
    def __init__(self, db):
        self._db = db

    def author(self, name):
        return pprint.pprint(self._db.posts.find_one({"author": name}))


class Put:
    pass


class Delete:
    pass


class Client:
    def __init__(self):
        self._user = os.environ['USER']
        self._pwd = os.environ['PWD']
        self._endpoint = os.environ['END']

        client = pymongo.MongoClient(
            "mongodb+srv://" + self._user + ":" + self._pwd + self._endpoint,
            ssl_cert_reqs=ssl.CERT_NONE
        )
        self._db = client.test

        self._post = Post()
        self._get = Get(self._db)
        self._delete = Delete()
        self._put = Put()

    def check_connection(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def get(self, name):
        pass

    def delete(self):
        pass

    @property
    def get(self):
        return self._get

    @property
    def delete(self):
        return self._delete

    @property
    def post(self):
        return self._post

    @property
    def put(self):
        return self._put


if __name__ == '__main__':
    c = Client()
    c.get.author('Scott')