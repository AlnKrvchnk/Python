import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client['pymongo']
posts = db.posts
post_1 = {
     'title': 'Pice and War',
     'content': '_',
     'author': 'Lev Tolstoy'
    }
post_2 = {
     'title': 'Evgeniy Onegin',
     'content': '~',
     'author': 'Pyskin'
    }
post_3 = {
     'title': 'Died Soul)',
     'content': '/',
     'author': 'Gogol'
    }
new_result = posts.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))
