from flask import Flask, request, render_template
from flask_restful import Resource, Api
import json
import os

with open('secret.json') as data_file:
    data = json.load(data_file)
    client_id = data['client_id']
    client_secret = data['client_secret']
    redirect_uri = ''
scopes = 'user-read-private user-read-email'

app = Flask(__name__)
api = Api(app)
todos={}
class HelloWorld(Resource):
    def get(self,todo_id):
        return {'hello': 'world',todo_id:todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id]= request.form['data']
        return {todo_id:todos[todo_id]}
class Connection(Resource):
    def get(get):
       return {}
api.add_resource(HelloWorld, '/todo/<string:todo_id>')

@app.route('/')
def hello(name=None):
    print(open('index.html'))
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
