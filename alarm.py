import os
import sys
import json
import RPi.GPIO as io
from webServer import *
import time

class alarm:
    alarmEndPoint = '/entrance/?format=json'
    alarmCount = 0
    alarms = []
    response = ''
    statusValues = {1:True,0:False}
    alarmStatus = [2,2,2,2,2]
    index = 0
    
    def initPorts(self):
        for alarm in self.alarms:
            io.setmode(io.BCM)
            io.setup(alarm['gpio'], io.IN, pull_up_down=io.PUD_UP)
            
    def registerAlarm(self,GPIO,label,type,webServer,raspberryPi):
        print 'Type: ' + str(type)
        data = {'raspberry_pi_id':raspberryPi.getId(),
			'status':False,
			'gpio':GPIO,
			'label':label,
			'entrance_type' :type
			}
        print data
        if webServer.postToDatabase(data,self.alarmEndPoint):
            return 'Alarm with GPIO: ' + str(GPIO) + ' successfully registered'
        else:
            return 'Probelm registering Alarm with GPIO: ' + str(GPIO)

    def updateAlarmInfo(self,alarm):
        self.alarms = alarm
	#This function is not needed
	#Only need updateAlarmInfo and updateAlarm to detect change in sensor
	#using this function along with the other two cuases alarmStatus to be
	#overwritten with new value before it is checked in updateAlarm 
    def updateStatus(self):
        for alarm in self.alarms:
            if alarm['alarm']:
                self.alarmStatus[self.index] =  io.input(alarm['gpio'])
            else:
                self.alarmStatus[self.index] = 2
            self.index = self.index + 1
        self.index = 0
    
    def updateAlarm(self,webServer,raspberryPi):
        for alarm in self.alarms:
            if alarm['alarm']:
                currentStatus = io.input(alarm['gpio'])
                if currentStatus != self.alarmStatus[self.index]:
                    self.alarmStatus[self.index] = currentStatus
                    data = {'raspberry_pi_id': raspberryPi.getId(),
                            'status': self.statusValues[currentStatus],
                            }
                    endPoint = '/entrance/' + str(alarm['id']) + '/?format=json'
                    self.response = webServer.putToDatabase(data,endPoint)
                    print 'Break in'
                else:
                    print 'System Normal'
            self.index= self.index + 1
        self.index = 0
                    
'''            
web = webServer()
web.setUsername('test7')
web.setPassword('test')
web.setAuth()
pi = raspberryPi(web)
door = alarm()
print door.registerAlarm(17,'Front Door', 'door', web, pi)
print door.registerAlarm(22,'Back Door', 'door', web, pi)
door.updateAlarmInfo(web)
door.initPorts()
door.updateStatus()

while 1:
	print 'Start Loop'
	door.updateAlarmInfo(web)
	door.updateAlarm(web,pi)
	time.sleep(1)
'''
