import os
import sys
import json

parentdir = os.path.dirname(os.path.abspath(__file__)) + '/requestsdir'
sys.path.insert(0, parentdir)

import requests
from requests.auth import HTTPBasicAuth
import RPi.GPIO as io

URL_ROOT = 'http://autopi.herokuapp.com/api/v1'
prevLights = {}

prevEntrances = None

def start(username,password):
	print 'In start()'
	print 'username: ' + username + ' password: ' + password
	initIO()
	auth=HTTPBasicAuth(username,password)
	user = getUser(auth)
	raspberryPi = getPi(user)
	lights = getLights(auth)
	entrances = getEntrances(auth)

	while True:
		lights = getLights(auth)
		updateLights(lights)
		
		updateEntrances(entrances,auth,raspberryPi['id'])
	

def updateLights(lights):
	print 'In updateLights'
	for light in lights:
		gpioPin = light['gpio']	
		print 'Light ' + str(light['label']) + ' status: ' + str(light['status']) + ' on pin ' + str(light['gpio'])
		if light['status'] == True:
			io.output(gpioPin, io.HIGH)	
		else:
			io.output(gpioPin, io.LOW)

def updateEntrances(entrances,auth,PiID):
	print 'In updateEntrances'
	global prevEntrances

	statusValues = {1:True,0:False}

	currentEntranceStatus = io.input(entrances['gpio'])
	print 'CurrentStatus'
	print currentEntranceStatus
	if currentEntranceStatus != prevEntrances:
		print'Status has changed'
		prevEntrances = currentEntranceStatus
		entranceID = entrances['id']

		params = {
			'raspberry_pi_id':PiID,
			'status':statusValues[currentEntranceStatus]}

		updateResponse = requests.put(
			'%s/entrance/%s/?format=json' % (URL_ROOT, entranceID),
			data = json.dumps(params),
			headers={'Content-type':'application/json'},
			auth=auth,
		)

		print 'updateResponse'
		print updateResponse

def getUser(auth):
	userResponse = requests.get(URL_ROOT+'/user/?format=json',auth=auth)
	allUserInfo = userResponse.json()
	user = allUserInfo['objects'][0]

	return user

def getPi(user):
	raspberryPi = user['raspberry_pi'][0]

	return raspberryPi

def getLights(auth):
	print 'In getLights'
	lightsResponse = requests.get(URL_ROOT+'/light/?format=json',auth=auth)
	light_count = lightsResponse.json()['meta']['total_count']

	lights = lightsResponse.json()['objects']

	return lights

def getEntrances(auth):
	print 'In getEntrances'
	entrancesResponse = requests.get(URL_ROOT+'/entrance/?format=json',auth=auth)
	entrance_count = entrancesResponse.json()['meta']['total_count']
	print entrancesResponse.json()
	entrances = entrancesResponse.json()['objects'][0]

	return entrances

def initIO():
	#set Pi BCM mode to access GPIO pins
	io.setmode(io.BCM)
	#set light pins to output mode
	io.setup(4, io.OUT)
	io.setup(17, io.OUT)
	io.setup(18, io.OUT)
	#set window/door pins to input mode and 
	#activate pull-up resistors
	io.setup(24, io.IN, pull_up_down=io.PUD_UP)
	io.setup(22, io.IN, pull_up_down=io.PUD_UP)
	
	
	
