

Requirements: https://github.com/balloob/pychromecast

Insallation:
- Install python-module pychromecast: sudo pip install pychromecast
- create dummy switch in domoticz: https://www.domoticz.com/wiki/Hardware_Setup#Dummy_Hardware
- get the IDX of the new switch (in devices-tab)
- Configure script:
	- Domoticz URL
	- IDX off dummy switdh
	- Chromecast-name

- Start the script after startup with command: `nohup python3 chromecast.py`.  (via Cron/rc.local/etc.)