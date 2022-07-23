#! /usr/bin/env python3

from relays import Relays, ON, OFF
import time

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
                r.relay1(p[0]) # red
                r.relay2(p[1]) # green
                r.relay3(p[2]) # blue
                time.sleep(1)
