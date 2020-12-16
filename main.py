#!/usr/bin/env python
 
 # Reference: https://www.ozeki.hu/p_3023-how-to-setup-a-nfc-reader-on-raspberry-pi.html

import signal
import time
import sys
import spotify
 
from pirc522 import RFID

NFC_TO_ALBUM = {
    88: "spotify:album:5ht7ItJgpBH7W6vJ5BqpPr",
    89: "spotify:album:2kHxP4JlbMnThrDoSwkb6y"
}
 
run = True
rdr = RFID()
util = rdr.util()
util.debug = True
 
def end_read(signal, frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()
 
 
signal.signal(signal.SIGINT, end_read)
 
print("Starting")
while run:
    (error, data) = rdr.request()
    if not error:
        print("\nDetected: " + format(data, "02x"))
 
    (error, uid) = rdr.anticoll()
    if not error:
        print("Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," +
                str(uid[2]) + "," + str(uid[3]))
        nfc_key = uid[2]

        spotify_album_uri = NFC_TO_ALBUM.get(nfc_key)
        spotify.play_album(spotify_album_uri)


 
        # print("Setting tag")
        # util.set_tag(uid)
        # print("\nAuthorizing")
        # # util.auth(rdr.auth_a, [0x12, 0x34, 0x56, 0x78, 0x96, 0x92])
        # util.auth(rdr.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
        # print("\nReading")
        # util.read_out(4)
        # print("\nDeauthorizing")
        # util.deauth()
 
        time.sleep(1)