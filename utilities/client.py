import pymongo
import ssl
import os


class Post:
    pass


class Get:
    pass


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
        db = client.test

        self._post = Post()
        self._get = Get()
        self._delete = Delete()
        self._put = Put()

    def check_connection(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def get(self):
        pass

    def delete(self):
        pass

if __name__ == '__main__':
    pass