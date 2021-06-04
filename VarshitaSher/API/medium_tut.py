# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 14:25:17 2020

@author: Diego
"""

'''
from flask import Flask 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    
    def get(self):
        return{'hello': 'world'}
    
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port = 12345)

'''

from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
api.add_resource(HelloWorld, '/')
if __name__ == '__main__':
    app.run(debug=True, port = 12345)