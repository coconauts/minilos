import requests 
import json
from spotify_keys import *
from pprint import pprint
import base64 

# https://developer.spotify.com/documentation/web-api/reference/player/

def refresh_headers(): 
    access_token = request_refresh_token(refresh_token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token
    }
    return headers

spotify_album_uri = "spotify:album:5ht7ItJgpBH7W6vJ5BqpPr"

def request_refresh_token(token):
  url = "https://accounts.spotify.com/api/token" 
  data = {
    "grant_type": "refresh_token",
    "refresh_token": token 
  }

  b64auth = "{}:{}".format(client_id,client_secret)
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic {}'.format(base64.b64encode(b64auth.encode("utf-8")).decode("utf-8"))
  }
  r = requests.post(url , headers=headers, data=data )

  print("status code {}".format(r.status_code))  
  print("request_token {}".format(r.text))  
  return r.json()['access_token']

def get_devices():
  url = "https://api.spotify.com/v1/me/player/devices"
  r = requests.get(url , headers=refresh_headers())

  #import pdb; pdb.set_trace()

  print("status code {}".format(r.status_code))  
  print("DEVICES: {}".format(r.json()))  

def currently_playing():
  url = "https://api.spotify.com/v1/me/player/currently-playing"
  r = requests.get(url , headers=refresh_headers())

  print("status code {}".format(r.status_code))  
  print("CURRENTLY PLAYING {}".format(r.json()))  


def play_album(spotify_album_uri=spotify_album_uri, device=device_id):
  url = "https://api.spotify.com/v1/me/player/play?device_id=" + device
  data = {
    "context_uri": spotify_album_uri,
    "offset": {
      "position": 5
    },
    "position_ms": 0
  }
  r = requests.put(url , headers=refresh_headers(), json=data )

  #import pdb; pdb.set_trace()

  print("status code {}".format(r.status_code))  
  print("PLAY {}".format(r.text))  

play_album()


