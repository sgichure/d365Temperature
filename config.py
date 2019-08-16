""" configuration options """

import machine
import ubinascii

DEVICE_MAC = ubinascii.hexlify(machine.unique_id()).upper()

WIFI_SSID = '<your wifi ssid name>'
WIFI_PASS = '<your wifi password>'

EVENT_GRID_TEMP_URL = '<specify your endpoint>'

 #Colors
off = 0x000000
red = 0xff0000
green = 0x00ff00
blue = 0x0000ff