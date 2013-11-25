from raspberryPi import *
from camera import *
from webServer import *
from light import *
from alarm import *


class register:
    def __init__(self,webServer,raspberryPi,light,camera,alarm):
        self.componentRegistration(webServer,raspberryPi,light,camera,alarm)
    
    def componentRegistration(self,webServer,raspberryPi,light,camera,alarm):
        #print raspberryPi.registerPi(webServer)
        #print light.registerLight(4,'Living Room',webServer,raspberryPi)
        #print light.registerLight(8,'Bed Room',webServer,raspberryPi)
        #cam.setIpAddress('69.243.172.96')
        #print cam.registerCamera(webServer,raspberryPi,'Living Room')
        print alarm.registerAlarm(24,'Front Door','door',webServer,raspberryPi)
        
        
        
        
web = webServer('shawn','shawn')
pi = raspberryPi(web)
cam = camera()
light = light()
alarm = alarm(web)
reg = register(web,pi,light,cam,alarm)