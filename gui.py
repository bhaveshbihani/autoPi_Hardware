import sys
import os
from Tkinter import *
import tkMessageBox
from webServer import *
import json
import ConfigParser
import requests
from requests.auth import HTTPBasicAuth

class registerGUI:
    homepath = '/home/pi'  
    loginEndPoint = '/user/?format=json'  
    def __init__(self, master,webServer):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='Username').grid(row=0, column=0)
        self.username = StringVar()
        Entry(frame, textvariable=self.username).grid(row=0,column=1)
        
        Label(frame, text='Password').grid(row=1, column=0)
        self.password = StringVar()
        Entry(frame, textvariable=self.password).grid(row=1, column=1)
        login_button = Button(frame, text='Login', command= lambda: self.getUser(webServer))
        login_button.grid(row=2)

    def getUser(self,webServer):
        webServer.setUsername(self.username.get())
        webServer.setPassword(self.password.get())
        webServer.setAuth()
        print('In getUser()')
        try:
            login_response = webServer.getFromDatabase(self.loginEndPoint)
        except:
            self.setNoInternetError()
            return
        print login_response
        
        if not login_response:
            self.setLoginError()
            return 
        self.createConfig()
        print self.SaveUser(self.homepath,self.username.get(),self.password.get())
        global root
        root.quit()		
   
	
    def setNoInternetError(self):
        tkMessageBox.showinfo('Error','No internet')
        print('No internet')

    def setLoginError(self):
        tkMessageBox.showinfo('Error','Login failed')
        print('Login error')

    def setRegisterError(self):
        tkMessageBox.showinfo('Error','Could not register ' + component + 'component.')
    
    def SaveUser(self,path,username,password):
        print('In autoPiStartup.SaveUser')
        config = ConfigParser.ConfigParser()
        config.read(path+'/autopi.config')
        config_file = open(path+'/autopi.config','w')
        config.add_section('LoginInfo')
        config.set('LoginInfo','Username',username)
        config.set('LoginInfo','Password',password)
        config.write(config_file)
        config_file.close()
        return True
        
    def createConfig(self):
         open(self.homepath+'/autopi.config','w').close()


    		

