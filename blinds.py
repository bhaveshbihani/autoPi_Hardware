import RPi.GPIO as io
from time import sleep
from time import clock
from webServer import *
from time import sleep

class blinds:
    time = .0005
    runTime = 1.5
    blinds = ''
    blindsEndPoint = '/blinds/?format=json'
    response = ''
    blindsStatus = [0,0,0,0,0]
    index = 0
    def __init__(self):
        io.setwarnings(False)
        io.setmode(io.BCM)
	io.setup(11,io.OUT)
	io.setup(9,io.OUT)
	io.setup(10,io.OUT)
	io.setup(7,io.OUT)
    def registerBlinds(self,GPIO,label,raspberryPi,webServer):
        data = {'raspberry_pi_id':raspberryPi.getId(),
			'status':False,
			'gpio':GPIO,
			'label':label}
	if webServer.postToDatabase(data,self.blindsEndPoint):
	    return 'Successfully registered Blinds'
	else:
	    return 'Error registering Blinds'
    
    def updateBlindInfo(self,blind):
        self.blinds = blind
    
    def initStatus(self):
        for blind in self.blinds:
            if blind['status']:
                self.blindsStatus[self.index] = 0
            else:
                self.blindsStatus[self.index] = 1
            self.index = self.index + 1
        self.index = 0

    def updateBlinds(self):
        for blind in self.blinds:
            if blind['status'] and self.blindsStatus[self.index] == 1 :
                print 'open'
                self.open()
                self.blindsStatus[self.index] = 0
            elif not blind['status'] and self.blindsStatus[self.index] == 0:
                print 'close'
                self.close()
                self.blindsStatus[self.index] = 1
            self.index = self.index + 1
        self.index = 0
    def open(self):
        startTime=clock()
        while True:
            currentTime = clock()
            if ( currentTime - startTime > self.runTime):
                break;		
            io.output(11,True)
            io.output(9,False)
            io.output(10,False)
            io.output(7,False)
            sleep(self.time)
        
            io.output(11,True)
            io.output(9,True)
            io.output(10,False)
            io.output(7,False)
            sleep(self.time)
			
            io.output(11,False)
            io.output(9,True)
            io.output(10,False)
            io.output(7,False)
            sleep(self.time)
        
            io.output(11,False)
            io.output(9,True)
            io.output(10,True)
            io.output(7,False)
            sleep(self.time)
        
            io.output(11,False)
            io.output(9,False)
            io.output(10,True)
            io.output(7,False)
            sleep(self.time)
        
            io.output(11,False)
            io.output(9,False)
            io.output(10,True)
            io.output(7,True)
            sleep(self.time)
        
            io.output(11,False)
            io.output(9,False)
            io.output(10,False)
            io.output(7,True)
            sleep(self.time)
        
            io.output(11,True)
            io.output(9,False)
            io.output(10,False)
            io.output(7,True)
            sleep(self.time)
        
    def close(self):
        startTime=clock()
        while True:
            currentTime = clock()
            if ( currentTime - startTime > self.runTime):
                break;	
            io.output(11,True)
            io.output(9,False)
            io.output(10,False)
            io.output(7,True)
            sleep(self.time)
			
            io.output(11,False)
            io.output(9,False)
            io.output(10,False)
            io.output(7,True)
            sleep(self.time)
        
            io.output(11,False)
            io.output(9,False)
            io.output(10,True)
            io.output(7,True)
            sleep(self.time)
        
            io.output(11,False)
            io.output(9,False)
            io.output(10,True)
            io.output(7,False)
            sleep(self.time)
        
            io.output(11,False)
            io.output(9,True)
            io.output(10,True)
            io.output(7,False)
            sleep(self.time)
        
            io.output(11,False)
            io.output(9,True)
            io.output(10,False)
            io.output(7,False)
            sleep(self.time)
        
            io.output(11,True)
            io.output(9,True)
            io.output(10,False)
            io.output(7,False)
            sleep(self.time)
        
            io.output(11,True)
            io.output(9,False)
            io.output(10,False)
            io.output(7,False)
            sleep(self.time)
    
      
#web = webServer('shawn','shawn')     
#blinds = blinds()
#while True:
#    blinds.updateBlinds(web)
#pi = raspberryPi(web)
#print blinds.registerBlinds(10,'Living Room',pi,web)
