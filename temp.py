import time
import pycom
from machine import Pin
from onewire import DS18X20
from onewire import OneWire

import sendhttp

#DS18B20 data line connected to pin P10 --> #G17 on Pycom expansion board
#     _____
#    |DS18 |
#    |_B20_|
#     / | \
#    1  2  3
#   
# 1. Ground
# 2. + 3.3 v
# 3. P10 - Maps to G17 on Pycom Board V2 and V3

  
ow = OneWire(Pin('P10')) 
temp = DS18X20(ow)
#pycom.heartbeat(False)
time.sleep(10)

for cycles in range (100): # stop after 10 cycles
#while True:       
    time.sleep(1)
    temp.start_conversion()
    time.sleep(1)
    currenttemp = temp.read_temp_async()
    sendhttp.sendToEventGrid(currenttemp)   
    print(currenttemp)
    time.sleep(7)