import Image
from camera import camera
from subprocess import call

class motion:
    currentImage = Image.new('RGB',(150,150),"black")
    prevImage = Image.new('RGB',(150,150),"black")
    alarmEndPoint = '/entrance/?format=json'
    camera = camera()
    width = 0
    height = 0
    totalMovement = 0
    def __init__(self):
        self.setPrevImage()
        self.setWidthHeight()
    def movement(self):
        self.setCurrentImage()
        currentImagePixels = self.currentImage.load()
        prevImagePixels = self.prevImage.load()
        x=0
        y=0
        
        while y<self.height:
            while x<self.width:
                p1,p2,p3 = currentImagePixels[x,y]
                c1,c2,c3 = prevImagePixels[x,y]
                difference = (p1 - c1) + (p2 - c2) + (p3 - c3)
                if difference > 20:
                    self.totalMovement +=1
                x+=1
            x=0
            y+=1
        print self.totalMovement
        self.prevImage = self.currentImage 
        if self.totalMovement > 500:
            self.totalMovement = 0
            return True
        else:
            self.totalMovement = 0
            return False
           
    def setCurrentImage(self):
        self.camera.takePicture('currentImage.jpg','150','150')
        self.currentImage=Image.open("/home/pi/Desktop/currentImage.jpg")
    def setPrevImage(self):
        self.camera.takePicture('prevImage.jpg','150','150')
        self.prevImage = Image.open("/home/pi/Desktop/prevImage.jpg")
    def setWidthHeight(self):
        self.width,self.height = self.prevImage.size
    def registerMotionAlarm(self,webServer)
        data = {'raspberry_pi_id':raspberryPi.getId(),
			'status':False,
			'gpio':30,
			'label':'Motion Alarm',
			'entrance-type' :'door'
			}
        if webServer.postToDatabase(data,self.alarmEndPoint):
            return 'Motion Alarm successfully registered'
        else:
            return 'Probelm registering Motion Alarm'

