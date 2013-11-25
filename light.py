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
    
    def __init__(self,webServer):
        self.response = webServer.getFromDatabase(self.lightEndPoint)
        self.totalLights = self.response.json()['meta']['total_count']
        self.lights = self.response.json()['objects']
    def setTotalLights(self,totalLights):
        self.totalLights = totalLIghts
    
    def updataStatus(self,webServer):
        print hello
    
    def registerLight(self,GPIO,label,webServer,raspberryPi):
        data = {'raspberry_pi_id':raspberryPi.getId(),
			'status':False,
			'gpio':GPIO,
			'label':label}
        if webServer.postToDatabase(data,self.lightEndPoint):
            return 'Light with GPIO: '+ str(GPIO) +' successfully registered'
        else:
            return 'Problem registering light with GPIO:',GPIO
        
        
#web = webServer('shawn','shawn')
#pi = raspberryPi(web)
#light = light(web)
#print light.registerLight(4,'Living Room',web,pi)