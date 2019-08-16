import machine
import pycom
import time
from network import WLAN
import Config


pycom.heartbeat(False)
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    if net.ssid == Config.WIFI_SSID:
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, Config.WIFI_PASS ), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        pycom.rgbled(Config.green)
        break
time.sleep(1.5)
pycom.rgbled(0x000000) #off

execfile('temp.py')
