from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import spotify

reader = SimpleMFRC522()

NFC_TO_ALBUM = {
    390: "spotify:album:1kCHru7uhxBUdzkm4gzRQc", # hamilton 
    927: "spotify:playlist:1kq332GEYrX6D5vrszgDUF", # dropmix
    460: "spotify:playlist:0uEOz6n3BoNGa39CQVtsbH", # life is strange
    997: "spotify:playlist:37i9dQZF1DZ06evO2hOiea", # nobuo uematsu
    530: "spotify:playlist:37i9dQZF1DWSNC7AjZWNry", # queen
}
 

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))

        last_3_chars = id % 1000
        spotify_uri = NFC_TO_ALBUM.get(last_3_chars)
        if not spotify_uri: 
            print("NFC not in dict {}".format(last_3_chars))
        else: 
            print("Playing {}".format(spotify_uri))
            spotify.play(spotify_uri)

        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
