from subprocess import call
from webServer import *
from os import system

class camera:
    ipAddress = '0.0.0.0'
    cameraEndPoint = '/video_stream/?format=json'
    response = ''
    camera = ''
    status = 0
	
    def takePicture(self,pictureName,pictureWidth,pictureHeight):
        call([ "raspistill","--nopreview","-t","500","-w",pictureWidth,"-h",pictureHeight,"-vf","-o",pictureName])
    
    def updateCameraInfo(self,webServer):
        self.response = webServer.getFromDatabase(self.cameraEndPoint)
        self.camera = self.response.json()['objects']
    
    def registerCamera(self,webServer,raspberryPi,label):
        data={
                'ip_address': self.ipAddress,
                'entrance_id': 1,
                'gpio': 1,
                'raspberry_pi_id': raspberryPi.getId(),
                'status': False,
                'label' : label
                }
        if webServer.postToDatabase(data,self.cameraEndPoint):
            return 'Camera successfully registered'
        else:
            return 'Error registering Camera'
    
    def setIpAddress(self,ipAddress):
        self.ipAddress = ipAddress
    
    def startCameraServer(self):
        call(["mjpg_streamer","-i","/usr/local/lib/input_file.so -f /tmp -n pic.jpg","-o","/usr/local/lib/output_http.so -w /usr/local/www -p 9000","-b"])
    
    def updateStatus(self,webServer):
        self.updateCameraInfo(webServer)
        for cam in self.camera:
            if cam['status'] == True and status = 0:
                call(["raspistill","--nopreview","-w","640","-h","480","-q","80","-o","/tmp/pic.jpg","-tl","100","-t","9999999","-vf","-th","0:0:0","&"])
                status = 1


#web = webServer()
#web.setUsername('shawn')
#web.setPassword('shawn')
#web.setAuth()
#pi = raspberryPi(web)
#cam = camera()
#cam.takePicture('shawn.jpg','50','50')
#cam.startCameraServer()
#while True:
#    cam.updateStatus(web)
#    print 'hello'

