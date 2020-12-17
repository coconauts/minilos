## Run with 
# export FLASK_APP=spotify_auth.py ; flask run 

from flask import Flask, escape, request
from spotify_keys import *
import urllib
import requests
import base64 
app = Flask(__name__)




def request_token(code):
  url = "https://accounts.spotify.com/api/token" 
  data = {
    "grant_type": "authorization_code",
    "code": code, 
    "redirect_uri": redirect_uri
  }

  b64auth = "{}:{}".format(client_id,client_secret)
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic {}'.format(base64.b64encode(b64auth.encode("utf-8")).decode("utf-8"))
  }
  r = requests.post(url , headers=headers, data=data )

  print("status code {}".format(r.status_code))  
  print("request_token {}".format(r.text))  


@app.route('/callback')
def callback():
    code = request.args.get('code')
    request_token(code)
    return "Done"

print("Oauth process started, click on this URL to begin auth")

scopes = 'user-read-private user-read-currently-playing user-modify-playback-state'
redirect_uri = "http://localhost:5000/callback"
auth_url = 'https://accounts.spotify.com/authorize?response_type=code&client_id={}&scope={}&redirect_uri={}'.format(
    client_id , urllib.parse.quote(scopes), urllib.parse.quote(redirect_uri)
) 

print(auth_url)

