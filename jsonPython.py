#!/usr/bin/python

import socket
import os 
import json

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(("", 1024))

print "Se espera conexion... Usando el puerto 1024"

serv.listen(1)

print "Escuchando..."

clie, addr = serv.accept()
while 1:
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    data = clie.recv(1024)

    #print 'DO: ' + data
    jsondata = json.loads(data)

    if  jsondata.get('volume') !=None:
    	print jsondata.get('volume')
    	cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to %s
            end tell'""" %jsondata.get('volume')
        os.system(cmd)
    elif jsondata.get('open') =="open":
    	print 2
    	cmd="""osascript -e 'tell application "iTunes" to activate'"""

    	os.system(cmd)
    elif jsondata.get('close') =='close':
    	print 3
    	cmd="""osascript -e 'tell application "iTunes" to quit'"""

    	os.system(cmd)
    elif jsondata.get('nextTrack') == "nextTrack":
    	print 4
    	cmd="""osascript -e 'tell application "iTunes" to play (next track)'"""
    	os.system(cmd)

    elif jsondata.get('play') == "play":
    	print 'si play'
    	cmd="""osascript -e 'tell application "iTunes" to tell application "iTunes" to playpause'"""
    	os.system(cmd)
    elif jsondata.get('trackBack') == "trackBack":
    	print 5
    	cmd="""osascript -e 'tell application "iTunes" to play (previous track)'"""
    	os.system(cmd)
    elif jsondata.get('trackName')!= None:
        print jsondata['trackName']
        cmd="""osascript -e 'tell application "iTunes" 
        play the track named "%s"
        end tell'"""%jsondata['trackName']
        os.system(cmd)



clie.close()
serv.close()
