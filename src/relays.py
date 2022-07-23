#! /usr/bin/env python3

from serial import Serial

ON = True
OFF = False

class Relays(Serial):
    def __init__(self, port='/dev/ttyUSB0'):
        super().__init__(port)
        self.dtr = False
        self.rts = False

    def relay1 (self, state):
        self.dtr = state

    def relay2 (self, state):
        self.rts = state

    def relay3 (self, state):
        self.break_condition = state
