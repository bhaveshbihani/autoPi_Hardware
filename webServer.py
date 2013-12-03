import sys
import json
from error import *
import requests
from requests.auth import HTTPBasicAuth
import urllib2


class webServer:
    urlRoot = 'http://autopi.herokuapp.com/api/v1'
    username = ''
    password = ''
    auth = ''
    data = ''
    response = ''

    def setPassword(self,password):
        self.password = password
        
    def setUsername(self,username):
        self.username = username
        
    def setAuth(self):
        self.auth = HTTPBasicAuth(self.username,self.password)
        
    def setData(self,data):
        self.data = data
        
    def getResponse(self):
        return self.response
        
    def postToDatabase(self,data,endPoint):
        self.setData(data)
        try:
            self.response = requests.post(
                self.urlRoot+endPoint,
		        data=json.dumps(data),
		        headers={'Content-type': 'application/json'},
		        auth=self.auth,
                timeout = 5
                )
        except:
            err = error()
            err.setNoNetworkError()
            self.response = requests.post(
                self.urlRoot+endPoint,
		        data=json.dumps(data),
		        headers={'Content-type': 'application/json'},
		        auth=self.auth,
                timeout = 10
                )
            
        if self.checkResponse(self.response):
            return True
        else:
            return False

    def putToDatabase(self,data,endPoint):
        self.setData(data)
        try:
            self.response = requests.put(
                self.urlRoot+endPoint,
		        data=json.dumps(data),
		        headers={'Content-type': 'application/json'},
		        auth=self.auth,
                timeout = 5
                )
        except:
            err = error()
            err.setNoNetworkError() 
            self.response = requests.put(
                self.urlRoot+endPoint,
		        data=json.dumps(data),
		        headers={'Content-type': 'application/json'},
		        auth=self.auth,
                timeout = 10
                )
            
        if self.checkResponse(self.response):
            return True
        else:
            return False
    def getFromDatabase(self,endPoint):
        try:
            self.response = requests.get(
               self.urlRoot + endPoint,
               auth=self.auth,
               timeout = 5
            )
        except:
            err = error()
            err.setNoNetworkError()
            self.response = requests.get(
               self.urlRoot + endPoint,
               auth=self.auth,
               timeout = 10
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
