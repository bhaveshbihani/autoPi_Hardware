from subprocess import call
from webServer import *
from raspberryPi import *

class camera:
    ipAddress = ''
    cameraEndPoint = '/video_stream/?format=json'
    
    def __init__(self):
        self.data =[]
	
    def takePicture(self,pictureName,pictureWidth,pictureHeight):
        call([ "raspistill","--nopreview","-t","500","-w",pictureWidth,"-h",pictureHeight,"-vf","-o",pictureName])
    
    def registerCamera(self,webServer,raspberryPi,label):
        data={
                'ip_address': self.ipAddress,
                'entrance_id': 1,
                'gpio': 1,
                'raspberry_pi_id': raspberryPi.getId(),
                'status': False,
                'label' : label
                }
        return webServer.postToDatabase(data,self.cameraEndPoint)
    
    def setIpAddress(self,ipAddress):
        self.ipAddress = ipAddress


web = webServer('shawn','shawn')
pi = raspberryPi(web)
cam = camera()
cam.setIpAddress('69.243.172.96')
print cam.registerCamera(web,pi,'Living Room')