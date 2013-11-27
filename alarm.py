import os
import sys
import json
import RPi.GPIO as io
from webServer import *
from raspberryPi import *

class alarm:
    alarmEndPoint = '/entrance/?format=json'
    alarmCount = 0
    alarms = ''
    response = ''
    statusValues = {1:True,0:False}
    alarmStatus = [2,2,2,2,2]
    index = 0
    
    def initPorts(self):
        for alarm in self.alarms:
            io.setup(alarm['gpio'], io.IN, pull_up_down=io.PUD_UP)
            
    def registerAlarm(self,GPIO,label,type,webServer,raspberryPi):
        data = {'raspberry_pi_id':raspberryPi.getId(),
			'status':False,
			'gpio':GPIO,
			'label':label,
			'type' :type
			}
        if webServer.postToDatabase(data,self.alarmEndPoint):
            return 'Alarm with GPIO: ' + str(GPIO) + ' successfully registered'
        else:
            return 'Probelm registering Alarm with GPIO: ' + str(GPIO)

    def updateAlarmInfo(self,webServer):
        self.response = webServer.getFromDatabase(self.alarmEndPoint)
        self.alarmCount = self.response.json()['meta']['total_count']
        self.alarms = self.response.json()['objects']
    
    def updateStatus(self):    
        for alarm in self.alarms:
            if alarm['alarm']:
                self.alarmStatus[self.index] =  io.input(alarm['gpio'])
            else:
                self.alarmStatus[self.index] = 2
            self.index = self.index + 1
        self.index = 0
    
    def updateAlarm(self,webServer,raspberryPi):
        self.updateAlarmInfo(webServer)
        for alarm in self.alarms:
            if alarm['alarm']:
                currentStatus = io.input(alarm['gpio'])
                if currentStatus != self.alarmStatus[self.index]:
                    self.alarmStatus[self.index] = currentStatus
                    data = {'raspberry_pi_id': raspberryPi.getId(),
                            'status': statusValues[currentStatus],
                            }
                    endPoint = '/entrance/' + str(alarm['id']) + '/?format=json'
                    self.response = webServer.putToDatabase(data,endPoint)
                    print 'Break in'
                else:
                    print 'System Normal'
            self.index= self.index + 1
        self.index = 0
                    
            
            