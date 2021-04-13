"Minilos", or "minyls". is an attempt to adapt the experience of owning and playing vinyl records to the digital age.

NFC-enabled mini-vynils are read with a raspberry-pi-powered record-player, which reads the album from the NFC chip and plays it on spotify using their REST API.


### References

We're using a RC522 NFC reader. Here's some documentation https://www.ozeki.hu/p_3023-how-to-setup-a-nfc-reader-on-raspberry-pi.html An image with the pinout is also included in this repo.

We're using the spotify API https://developer.spotify.com/documentation/web-api/reference/player/

Spotify AUTH guide https://developer.spotify.com/documentation/general/guides/authorization-guide/

Spotify APP dashboard https://developer.spotify.com/dashboard/applications

### How to authenticate

First run ` export FLASK_APP=spotify_auth.py ; flask run --host=0.0.0.0` 
then click on the `/authorize` endpoint that will appear on the console 
This will take you to a browser where you can login
The callback will request a final token for your user
Copy the `refresh_token` in a new variable in `spotify_keys.py` file
This refresh token will be used to get a brand new auth_token everytime you make a request 

