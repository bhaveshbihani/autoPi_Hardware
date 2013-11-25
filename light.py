import os
import sys
import json
from webServer import *
from raspberryPi import *
import RPi.GPIO as io

class light:
    totalLights = 0
    response = ''
    lightEndPoint = '/light/?format=json'
    lights = ''
       
    def setTotalLights(self,totalLights):
        self.totalLights = totalLIghts
    
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
        
        
#web = webServer('shawn','shawn')
#pi = raspberryPi(web)
#light = light(web)
#light.updateStatus(web)