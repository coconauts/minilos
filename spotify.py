import requests 
import json
from spotify_keys import *
from pprint import pprint
import base64 
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

# https://developer.spotify.com/documentation/web-api/reference/player/
TIMEOUT = 5

def refresh_headers(): 
    access_token = request_refresh_token(refresh_token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token
    }
    return headers


def request_refresh_token(token):
  print("Requesting refresh token")

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
  r = http.post(url , headers=headers, data=data, timeout=TIMEOUT )

  #print("request_refresh_token response: {}".format(r.status_code))  
  #print("request_token {}".format(r.text))  
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


def play(spotify_uri, device=device_id):
  url = "https://api.spotify.com/v1/me/player/play?device_id=" + device
  data = {
    "context_uri": spotify_uri,
    "position_ms": 0
  }
  headers = refresh_headers()

  print("Playing {} on device {}".format(spotify_uri, device))

  r = http.put(url , headers=headers, json=data, timeout=TIMEOUT )

  #import pdb; pdb.set_trace()

  #print("play response: {}".format(r.status_code))  
  #print("PLAY {}".format(r.text))  

# test 
#spotify_album_uri = "spotify:album:5ht7ItJgpBH7W6vJ5BqpPr"

#play("spotify:album:5ht7ItJgpBH7W6vJ5BqpPr")


#get_devices()
