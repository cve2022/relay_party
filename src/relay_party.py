#! /usr/bin/env python3

from relays import Relays, RELAY1, RELAY2, RELAY3, ON, OFF
import time

RED   = RELAY1
GREEN = RELAY2
BLUE  = RELAY3

PATTERN1 = (
    (ON,  OFF, OFF),
    (OFF, ON,  OFF),
    (OFF, OFF, ON ),
)
PATTERN2 = (
    (OFF, OFF, ON ),
    (OFF, ON,  OFF),
    (ON,  OFF, OFF),
)
PATTERNS = (PATTERN1, PATTERN2)

r=Relays()
while True:
    for patt in PATTERNS:
        for i in range(4):
            for p in patt:
                print (p)
                r.relay(RED,   p[0])
                r.relay(GREEN, p[1])
                r.relay(BLUE,  p[2])
                time.sleep(1)
