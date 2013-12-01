from raspberryPi import *
from camera import *
from webServer import *
from light import *
from alarm import *


class register:
    def __init__(self,webServer,raspberryPi,light,camera,alarm,blind):
        self.componentRegistration(webServer,raspberryPi,light,camera,alarm,blind)
    
    def componentRegistration(self,webServer,raspberryPi,light,camera,alarm,blind):
        print raspberryPi.registerPi(webServer)
        raspberryPi.getPiData(webServer)
        print light.registerLight(4,'Living Room',webServer,raspberryPi)
        print light.registerLight(8,'Bed Room',webServer,raspberryPi)
        camera.setIpAddress('69.243.172.96')
        print camera.registerCamera(webServer,raspberryPi,'Living Room')
<<<<<<< HEAD
        print alarm.registerAlarm(24,'Front Door','door',webServer,raspberryPi)
        print blind.registerBlinds(5,'Living Room',raspberryPi,webServer)
=======
        print alarm.registerAlarm(22,'Front Door','door',webServer,raspberryPi)
        print alarm.registerAlarm(17,'Back Door','door',webServer,raspberryPi)
#        print blind.registerBlinds(5,'Living Room',raspberryPi,webServer)
>>>>>>> fe1b11be679c8361120e7c5e67a294bf0cd2a15f
        
        
        
#web = webServer()
#web.setUsername('shawn1')
#web.setPassword('shawn')
#web.setAuth()
#pi = raspberryPi(web)
#print pi.registerPi(web)
