from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import spotify

reader = SimpleMFRC522()

NFC_TO_ALBUM = {
    390: "spotify:album:1kCHru7uhxBUdzkm4gzRQc", # hamilton 
    927: "spotify:playlist:1kq332GEYrX6D5vrszgDUF", # dropmix
    460: "spotify:playlist:0uEOz6n3BoNGa39CQVtsbH", # life is strange
    530: "spotify:playlist:37i9dQZF1DWSNC7AjZWNry", # queen
    
    509: "spotify:album:1KCiWQIQtagNrWcJvPTiNe", #trance best of 
    423: "spotify:playlist:3NkBXHqVwjeyu5fcBcmIRE", #bioshock inspired
    983: "spotify:playlist:684nXqMbtn1gr1sNSk1MsI", #rock and roll
    176: "spotify:playlist:5gIPHDwAG2QN38CIdRW2y8", #persona 5
    131: "spotify:album:4CuBPBeJ8ncHwgQhIgvx2j", #destiny 2 : forsaken
    835: "spotify:album:1BNQflQCNLW3h9EMWZqpHm", # gentle love: game music lullabies

}

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
