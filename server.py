from flask import Flask, request
from flask_restful import Resource, Api
import json

with open('secret.json') as data_file:
    data = json.load(data_file)
    client_id = data['client_id']
    client_secret = data['client_secret']
    redirect_uri = ''


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
api.add_resource(HelloWorld, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
