import sys
import json
import requests
from requests.auth import HTTPBasicAuth


class webServer:
    urlRoot = 'http://autopi.herokuapp.com/api/v1'
    username = ''
    password = ''
    auth = ''
    data = ''
    response = ''
    def __init__(self,username,password):
        print username,password
        self.setUsername(username)
        self.setPassword(password)
        self.setAuth(username,password)

    def setPassword(self,password):
        self.password = password
        
    def setUsername(self,username):
        self.username = username
        
    def setAuth(self,username,password):
        self.auth = HTTPBasicAuth(username,password)
        
    def setData(self,data):
        self.data = data
        
    def getResponse(self):
        return self.response
        
    def postToDatabase(self,data,endPoint):
        self.setData(data)
        self.response = requests.post(
                self.urlRoot+endPoint,
		data=json.dumps(data),
		headers={'Content-type': 'application/json'},
		auth=self.auth
        )
        if self.checkResponse(self.response):
            return True
        else:
            return False
    def getFromDatabase(self,endPoint):
        self.response = requests.get(
               self.urlRoot + endPoint,
               auth=self.auth
        )
        if self.checkResponse(self.response):
            return self.response
        else:
            return False
    
    def checkResponse(self,response):
        if response.status_code not in [201,200]:
                return False
        else:
            return True
        

