from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import spotify
from album_mapping import NFC_TO_ALBUM
import RPi.GPIO as GPIO  

reader = SimpleMFRC522()



last_uri = ""

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))

        last_3_chars = id % 1000
        spotify_uri = NFC_TO_ALBUM.get(last_3_chars)
        if not spotify_uri: 
            print("NFC not in dict {}".format(last_3_chars))
        elif spotify_uri != last_uri: # Don't play it twice
            last_uri = spotify_uri
            print("Playing {}".format(spotify_uri))
            spotify.play(spotify_uri)

        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
