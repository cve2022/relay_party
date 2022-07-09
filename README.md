# relay_party

A simple example of the use of Python to control external devices from a PC through a USB-UART converter with C-MOS/TTL inputs/outputs.

Constituted by a class that abstracts the USB-UART converter outputs to outputs to control relays (with active low control inputs) and an example script that controls a string of RGB LEDs performing simple patterns to demonstrate the functioning of the class.

Tested with adapters based on CH340G (advertized as Adapter USB-UART CH340 for the WiFi ESP-01 ESP8266 module), FT232RL and CP2101N. The adapter based on CH340G requires some wiring to use the IC outputs)
