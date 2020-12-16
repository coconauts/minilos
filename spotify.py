import requests 
import json
from spotify_keys import *

# https://developer.spotify.com/documentation/web-api/reference/player/
print(oauth_token)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + oauth_token
    }


spotify_album_uri = "spotify:album:5ht7ItJgpBH7W6vJ5BqpPr"


def get_devices():
  url = "https://api.spotify.com/v1/me/player/devices"
  r = requests.get(url , headers=headers)

  import pdb; pdb.set_trace()

  print("status code {}".format(r.status_code))  
  print("DEVICES: {}".format(r.json()))  

def currently_playing():
  url = "https://api.spotify.com/v1/me/player/currently-playing"
  r = requests.get(url , headers=headers)

  print("status code {}".format(r.status_code))  
  print("CURRENTLY PLAYING {}".format(r.json()))  


def play_album(spotify_album_uri), device=office_device:
  url = "https://api.spotify.com/v1/me/player/play?device_id=" + device
  data = {
    "context_uri": spotify_album_uri,
    "offset": {
      "position": 5
    },
    "position_ms": 0
  }
  r = requests.put(url , headers=headers, json=data )

  import pdb; pdb.set_trace()

  print("status code {}".format(r.status_code))  
  print("PLAY {}".format(r.text))  

from pprint import pprint
get_devices()

a = "foo"
