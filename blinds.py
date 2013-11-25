import RPi.GPIO as io
from time import sleep
from time import clock

class blinds:
    time = .0015
    runTime = 1.5
    def __init__(self):
        io.setmode(io.BCM)
	io.setup(11,io.OUT)
	io.setup(9,io.OUT)
	io.setup(10,io.OUT)
	io.setup(7,io.OUT)
    def up(self):
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
        
    def down(self):
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
    
    def test(self):
        startTime=clock()
        while True:
            currentTime = clock()
            print currentTime - startTime
            if ( currentTime - startTime > self.runTime):
                break;		
            io.output(11,False)
            io.output(9,True)
            io.output(10,True)
            io.output(7,False)
            sleep(self.time)
        
            io.output(11,False)
            io.output(9,False)
            io.output(10,True)
            io.output(7,True)
            sleep(self.time)
			
            io.output(11,True)
            io.output(9,False)
            io.output(10,False)
            io.output(7,True)
            sleep(self.time)
        
            io.output(11,True)
            io.output(9,True)
            io.output(10,False)
            io.output(7,False)
            sleep(self.time)    
     

