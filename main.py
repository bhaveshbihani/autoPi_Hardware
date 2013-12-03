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
from error import *
import urllib2

web=webServer()	
err = error()
#Check network connection
if not web.testNetwork():
    err.setNoNetworkError()

homepath = '/home/pi/'
print homepath
print os.path.exists(homepath + '/autopi.config')
if not os.path.exists(homepath + '/autopi.config'):
    print 'no user info'
    root = Tk()
    root.wm_title('AutoPi Login')
    app = registerGUI(root,web)
    root.mainloop()

    print 'Web' 
    print web
    
    pi = raspberryPi(web)
    light = light()
    cam = camera()
    alarm = alarm()
    blind = blinds()
    reg = register(web,pi,light,cam,alarm,blind)
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
    if not pi.response:
        err.setLoginError()	
    light = light()
    cam = camera()
    alarm = alarm()
    blind = blinds()


#reg = register(web,pi,light,cam,alarm,blind)
pi.updatePiInfo(web,light,blind,alarm)  
alarm.initPorts()
alarm.updateStatus() 
light.setPins()
#cam.startCameraServer()
blind.initStatus()

while True:
    pi.updatePiInfo(web,light,blind,alarm)
    light.updateStatus()
    alarm.updateAlarm(web,pi)
    blind.updateBlinds()	
#    cam.updateStatus(web)

    print 'loop'
