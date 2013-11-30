import os
import sys
import json
from webServer import *
from raspberryPi import *
import RPi.GPIO as io

class light:
    response = ''
    lightEndPoint = '/light/?format=json'
    lights = ''
       
    
    def setPins(self):
        for light in self.lights:
            gpioPin = light['gpio']
            io.setup(gpioPin,io.OUT)
    
    def updateLightInfo(self,webServer):
        self.response = webServer.getFromDatabase(self.lightEndPoint)
        self.totalLights = self.response.json()['meta']['total_count']
        self.lights = self.response.json()['objects']
        
    def updateStatus(self,webServer):
        self.updateLightInfo(webServer)
        for light in self.lights:
            gpioPin = light['gpio']
            if light['status'] == True:
                io.output(gpioPin,io.HIGH)
            else:
                io.output(gpioPin,io.LOW)
    
    def registerLight(self,GPIO,label,webServer,raspberryPi):
        data = {'raspberry_pi_id':raspberryPi.getId(),
			'status':False,
			'gpio':GPIO,
			'label':label}
        if webServer.postToDatabase(data,self.lightEndPoint):
            return 'Light with GPIO: '+ str(GPIO) +' successfully registered'
        else:
            return 'Problem registering light with GPIO: '+str(GPIO)
        
'''        
web = webServer()
web.setUsername('test7')
web.setPassword('test')
web.setAuth()
pi = raspberryPi(web)
print pi.registerPi(web)
pi.getPiData(web)
light = light()
light.registerLight(4, 'Living Room',web,pi)
light.registerLight(8, 'Kitchen',web,pi)
light.updateLightInfo(web)
light.setPins()
while 1:
	light.updateStatus(web)
'''
