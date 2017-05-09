from flask import Flask, request, render_template
from flask_restful import Resource, Api
import json, requests
import os
with open('secret.json') as data_file:
    data = json.load(data_file)
    client_id = data['client_id']
    client_secret = data['client_secret']
    redirect_uri = ''
scopes = 'user-read-private user-read-email'
def get_attribute(access_token):
    url = 'https://api.spotify.com/v1/me/player/currently-playing'

    params = dict(
        access_token=access_token
    )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    track_id = data["item"]["id"]
    print(track_id)
    url = "https://api.spotify.com/v1/audio-analysis/"+track_id
    resp = requests.get(url=url,params=params)
    data = json.loads(resp.text)
    mode =data["track"]["mode"]
    mode_confidence =data["track"]["mode_confidence"]
    loudness = data["track"]["loudness"]
    tempo = data["track"]["tempo"]
    time_signature = data["track"]["time_signature"]
    time_signature_confidence = data["track"]["time_signature_confidence"]
    key = data["track"]["key"]
    key_confidence = data["track"]["key_confidence"]
    url = "https://api.spotify.com/v1/audio-features/"+track_id
    resp = requests.get(url=url,params=params)
    data = json.loads(resp.text)
    energy = data["energy"]
    danceability = data["danceability"]
    return [danceability,energy,key,key_confidence,loudness,mode,mode_confidence,tempo,time_signature,time_signature_confidence]
def get_track(artist,title):
    tracks=[]
    url = "https://api.spotify.com/v1/search?q=abba&type=track&q="+artist+" "+title
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    for i in data["tracks"]["items"]:
        tracks.append(i["id"])
    return tracks
# print(get_attribute(""))
# print(get_track("",""))
app = Flask(__name__)
api = Api(app)
todos={}
class HelloWorld(Resource):
    def get(self):
        print(self['access_token'])
        return {'hello': 'world'}

class Connection(Resource):
    def get(get):
       return {}
api.add_resource(HelloWorld, '/callback2')

@app.route('/')
def hello(name=None):
    access_token = request.args.get('access_token')
    print(access_token)
   # print(get_attribute(access_token))
    # print(get_track("",""))
    print(open('index.html'))
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)

