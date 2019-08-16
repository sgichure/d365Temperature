import Config
import pycom
import time
try:
    import urequests as requests
except ImportError:
    import requests

def sendToEventGrid(temperature):    
    url = Config.EVENT_GRID_TEMP_URL
    #http post json data containing mac adress and temperature
    res = requests.post(url,json={'macAddress': Config.DEVICE_MAC, 'temperature': temperature })
    res.close()

    if(res.status_code - 200) <100:
        print('Sent')        
        pycom.rgbled(Config.blue)
        time.sleep_ms(1000) #Wait for 1 Second
        pycom.rgbled(Config.off)
    else:
        print(':-( Something went wrong')
        pycom.rgbled(Config.red)
        time.sleep_ms(1000) #Wait for 1 Second
        pycom.rgbled(Config.off)

