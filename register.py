import sys
import json
import requests
from requests.auth import HTTPBasicAuth
from uuid import getnode as get_mac

URL_ROOT = 'http://autopi.herokuapp.com/api/v1'

def registerPi(username, password):
	print('In registerPi')
	auth = HTTPBasicAuth(username, password)

	mac =124999  # get_mac()
	print('mac: ' + str(mac))

	data = {'uuid': mac}
	raspi_resp = requests.post(
		URL_ROOT+'/raspberry_pi/?format=json',
		data=json.dumps(data),
		headers={'Content-type': 'application/json'},
		auth=auth
	)

	print('raspi_resp: ')
	print(raspi_resp)

	if raspi_resp.status_code not in [201,200]:
		print('raspi_resp not in [201,200]')
		print(raspi_resp)
		print(raspi_resp.json())
		return False

	return True

def defaultComponentRegistration(username,password):
	print('In defaultComponentRegistration.')
	auth = HTTPBasicAuth(username,password)
	userResponse = requests.get(URL_ROOT+'/user/?format=json',auth=auth)
	allUserInfo = userResponse.json()
	user = allUserInfo['objects'][0]
	raspberryPi = user['raspberry_pi'][0]
	headers = {'Content-type':'application/json'}

	#Create light on Pin 4 with Label 'Light One' set to initial state=off
	data = {'raspberry_pi_id':raspberryPi['id'],
			'status':False,
			'gpio':4,
			'label':'Light One'}

	#Register light
	light_response = requests.post(URL_ROOT+'/light/?format=json',data=json.dumps(data),headers=headers,auth=auth)
	print('Light 1')
	print(light_response)
	print(light_response.json())

	#Create light on Pin 17 with Label 'Light Two' set ot initial state=on
	data['status'] = True
	data['gpio']  = 17
	data['label'] = 'Light Two'

	#Register light
	light_response = requests.post(URL_ROOT+'/light/?format=json',data=json.dumps(data),headers=headers,auth=auth)
	print('Light 2')
	print(light_response)
	print(light_response.json())

	#Create light on Pin 18 with Label 'Light Two' set ot initial state=on
	data['status'] = True
	data['gpio']  = 18
	data['label'] = 'Light Three'
	
	#Register light
	light_response = requests.post(URL_ROOT+'/light/?format=json',data=json.dumps(data),headers=headers,auth=auth)
	print('Light 2')
	print(light_response)
	print(light_response.json())
	#Create door on Pin 24 with Label 'Front Door'
	data['gpio'] = 24
	data['label'] = 'Front Door'
	data['type'] = 'door'

	#Register door
	entrance_response = requests.post(URL_ROOT+'/entrance/?format=json',data=json.dumps(data),headers=headers,auth=auth)
	print('Front Door')
	print(entrance_response)
	print(entrance_response.json())

	#Create window on Pin 22 with Label 'Living Room Window'
	data['gpio'] = 22
	data['label'] = 'Living Room Window'
	data['type'] = 'window'

	#Register Window 
	entrance_response = requests.post(URL_ROOT+'/entrance/?format=json',data=json.dumps(data),headers=headers,auth=auth)
	print('Living Room Window')
	print(entrance_response)
	print(entrance_response.json())
