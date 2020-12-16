import requests 
import json
import spotify_keys

# https://developer.spotify.com/documentation/web-api/reference/player/

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Authorization': f'Bearer {oauth_token}'
    }
url = 'https://api.spotify.com/v1/me/player/devices'
r = requests.get(url , headers=headers)

print(f"status code {r.status_code}")  
print(f"DEVICES {r.json()}")  


url = 'https://api.spotify.com/v1/me/player/currently-playing'
r = requests.get(url , headers=headers)

print(f"status code {r.status_code}")  
print(f"CURRENTLY PLAYING:  {r.json()}")  

spotify_album_uri = "spotify:album:5ht7ItJgpBH7W6vJ5BqpPr"


url = f'https://api.spotify.com/v1/me/player/play?device_id={office_device}'
data = {
  "context_uri": spotify_album_uri,
  "offset": {
    "position": 5
  },
  "position_ms": 0
}
r = requests.put(url , headers=headers, json=data )

print(f"status code {r.status_code}")  
print(f"PLAY {r.text}")  
