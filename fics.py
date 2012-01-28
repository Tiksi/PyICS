#Telnet connection for freechess

import os
import logging
import telnetlib

HOST = "freechess.org" #69.36.243.188
PORT = 5000

USER = "7UP"
PASS = ''

contact = 'reason71944@gmail.com'

tn = telnetlib.Telnet(HOST)

endTime = 15

FingerData = ""

saveArea = "save.txt"

Ignore = ['RoboAdmin','Mamer', 'Relay'] #Welcoming bots that are annoying. This may change later

Connected = False


logger = logging.getLogger("Mr.Logger 1")
logger.setLevel(logging.DEBUG) #set the level to debug status

LeLogger = logging.StreamHandler() #get ready to output
LeLogger = logging.setLevel(logging.DEBUG) #set handler to debug status

format = logging.Formatter("$(asctime)s - %(name)s - %(levelname)s - %(message)s")  #format the message
LeLogger.setFormatter(format)
logger.addHandler(LeLogger)

##Testing
#
#logger.debug("debug message")
#
#
##