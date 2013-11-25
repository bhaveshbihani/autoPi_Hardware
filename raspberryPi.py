import os
import sys
import json
from webServer import *
from uuid import getnode as getMac


class raspberryPi:
    allUserInfo = ''
    user = ''
    raspberryPi = ''
    id = 0
    userEndPoint = '/user/?format=json'
    piEndPoint = '/raspberry_pi/?format=json'
    response = ''
    mac = 0
    def __init__(self,webServer):
        self.getPiData(webServer)
        self.mac = getMac()
    def registerPi(self,webServer):
        data = {'uuid': self.mac}
        if webServer.postToDatabase(data,self.piEndPoint):
            return 'RaspberryPi successfully register'
        else:
            return 'Problem registering RaspberryPi'
    def getPiData(self,webServer):
        self.response = webServer.getFromDatabase(self.userEndPoint)
        self.allUserInfo = self.response .json()
        self.user = self.allUserInfo['objects'][0]
        if self.user['raspberry_pi']:
            self.raspberryPi = self.user['raspberry_pi'][0]
            self.id = self.raspberryPi['id']
        else:
            print 'no device found'
    def getId(self):
        return self.id
        
        
#web = webServer('shawn','shawn')
#pi = raspberryPi(web)
