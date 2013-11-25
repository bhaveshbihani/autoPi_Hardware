from subprocess import call


class camera:
	def __init__(self):
		self.data =[]
	
	def takePicture(self,pictureName,pictureWidth,pictureHeight):
		call([ "raspistill","--nopreview","-t","500","-w",pictureWidth,"-h",pictureHeight,"-vf","-o",pictureName])

