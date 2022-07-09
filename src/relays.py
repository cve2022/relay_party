#! /usr/bin/env python3

from serial import Serial

ON = True
OFF = False

RELAY1 = 0
RELAY2 = 1
RELAY3 = 2

class Relays(Serial):
    def __init__(self, port='/dev/ttyUSB0'):
        super().__init__(port)
        self.dtr = False
        self.rts = False

    def relay (self, id, state):
        if id == RELAY1:
            self.dtr = state
        elif id == RELAY2:
            self.rts = state
        elif id == RELAY3:
            self.break_condition = state
        else:
            pass
