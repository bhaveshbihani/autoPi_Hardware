import sys
import os
from Tkinter import *
import tkMessageBox
import requests
import json
from light import *
from register import *
from webServer import *
from camera import *
from alarm import *
from blinds import *
from gui import *

web=webServer()	
homepath = '/home/pi/'
print homepath
print os.path.exists(homepath + '/autopi.config')
if not os.path.exists(homepath + '/autopi.config'):
    print 'no user info'
    root = Tk()
    root.wm_title('AutoPi Login')
    app = registerGUI(root,web)
    root.mainloop()
    
    pi = raspberryPi(web)
    light = light()
    cam = camera()
    alarm = alarm()
    blind = blinds()
    reg = register(web,pi,light,camera,alarm,blind)
else:
    config = ConfigParser.ConfigParser() 
    config.read(homepath+'/autopi.config')
    username = config.get('LoginInfo','username')
    password = config.get('LoginInfo','password')
    print 'working'
    web.setUsername(username)
    web.setPassword(password)
    web.setAuth()
    pi = raspberryPi(web)
    light = light()
    cam = camera()
    alarm = alarm()
    blind = blinds()

alarm.updateAlarmInfo(web)    
alarm.updateStatus() 
alarm.initPorts()
light.updateLightInfo(web)
light.setPins() 

while True:
    light.updateStatus(web)
    alarm.updateAlarm(web,pi)
    blind.updateBlinds(web)	



