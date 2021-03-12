"Minilos" (or "minyls") is an attempt to adapt the experience of owning and playing vinyl records to the digital age.

NFC-enabled mini-vynils are read with a raspberry-pi-powered record-player, which reads the album from the NFC chip and plays it on spotify using their REST API.


### References

We're using an MFRC522 NFC reader, and using the following library: https://github.com/pimylifeup/MFRC522-python. The library is bundled in this repo for convenience (you can find it in the `mfrc522` directory). To install the dependencies, go into the directory and run `python setup.py install`.

An image with the pinout to connect the reader module to the RPi is also included, on `NFC_MFRC522_RPI.png`.

We're using the spotify API https://developer.spotify.com/documentation/web-api/reference/player/

Spotify AUTH guide https://developer.spotify.com/documentation/general/guides/authorization-guide/

Spotify APP dashboard https://developer.spotify.com/dashboard/applications

### How to authenticate

First run ` export FLASK_APP=spotify_auth.py ; flask run` 
then click on the `/authorize` endpoint that will appear on the console 
This will take you to a browser where you can login
The callback will request a final token for your user
Copy the `refresh_token` in a new variable in `spotify_keys.py` file
This refresh token will be used to get a brand new auth_token everytime you make a request.

### Personalize your minilos

The file `album_mapping.py` contains a mapping from NFC tag IDs to spotify album/playlist/song URIs. Add your own!
