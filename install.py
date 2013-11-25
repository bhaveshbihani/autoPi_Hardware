#!/usr/bin/python2.7
from subprocess import call

call(["sudo","apt-get","install","python-setuptools","-y"])
call(["sudo","easy_install","pip"])
call(["sudo","pip","install","requests"])
call(["sudo","apt-get","install","python-tk","-y"])
call(["sudo","apt-get","install","python-dev","-y"])
call(["sudo","apt-get","install","python-rpi.gpio","-y"])