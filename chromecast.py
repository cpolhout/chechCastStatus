from __future__ import print_function
import time
import sys
import logging
import json
import codecs
import urllib
import pychromecast


#Domoticz baseURL
domoticz = "http://localhost"

#Domoticz switch IDX
idx=963

# Your Chromecast device Friendly Name
device_friendly_name = "Cast wk"

chromecasts = pychromecast.get_chromecasts()
# select Chromecast device
cast = next(cc for cc in chromecasts if cc.device.friendly_name == device_friendly_name)
# wait for the device
cast.wait()
print(cast.device)
print(cast.status)

class mediaListener:
  domurl=domoticz
  device=idx
  def __init__(self, domoticzurl, deviceno):
    self.domurl = domoticzurl
    self.device=str(deviceno)
    self.oldPlayerStatus = 'NONE'
  def new_media_status(self, status):
    print("mediaListener")
    print(status.player_state + " vs " + self.oldPlayerStatus)
    if (self.oldPlayerStatus != status.player_state):
      self.oldPlayerStatus = status.player_state
      print("Updating status to Domoticz: " + self.domurl + "/json.htm?type=command&param=switchlight&idx=" + self.device + "&switchcmd=xx")
      if status.player_state == "PLAYING" or status.player_state == "BUFFERING":
        data = urllib.urlopen(self.domurl + "/json.htm?type=command&param=switchlight&idx=" + self.device + "&switchcmd=On")
        print(data.geturl())
        print(data.read())
      else :
        data = urllib.urlopen(self.domurl + "/json.htm?type=command&param=switchlight&idx=" + self.device + "&switchcmd=Off")
        print(data.geturl())
        print(data.read())
        #self.storeVariable('ChromeState', new_state)

listener = mediaListener(domoticz, idx)

cast.media_controller.register_status_listener(listener)

while (1):
  pass