import RPi.GPIO as io
import time
import urllib2

class error:
	def __init__(self):
		io.setmode(io.BCM)
		io.setup(18,io.OUT)
		io.output(18,io.LOW)

	def setNoNetworkError(self):
		print 'No network'
		self.errorLight(0.5)

	def setLoginError(self):
		print 'Login Error'
		self.errorLight(1)

	def setRegisterError(self):
		print 'Registration Error'
		self.errorLight(2)

	def errorLight(self,delay):
		while 1:
			io.output(18,io.HIGH)
			time.sleep(delay)
			io.output(18,io.LOW)
			time.sleep(delay)
			print 'Network connection: ' +  str(self.testNetwork())
			if self.testNetwork():
				break

	def testNetwork(self):
		try:
			response = urllib2.urlopen('http://74.125.228.100',timeout=1)
			return True
		except urllib2.URLError as err:
			pass
		return False
