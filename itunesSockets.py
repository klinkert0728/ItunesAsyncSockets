#!/usr/bin/python

import socket
import os 

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(("", 1024))

print "Se espera conexion... Usando el puerto 1024"

serv.listen(1)

print "Escuchando..."

clie, addr = serv.accept()

while 1:
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    data = clie.recv(1024)

    print 'DO: ' + data
    #dic = json.loads(data)

    if data == "play":
    	cmd="""osascript -e 'tell application "iTunes" to tell application "iTunes" to playpause'"""
    	os.system(cmd)
    	
    elif data == "nextTrack":
    	cmd="""osascript -e 'tell application "iTunes" to play (next track)'"""
    	os.system(cmd)
    
    elif data == "trackBack":
        cmd="""osascript -e 'tell application "iTunes" to play (previous track)'"""
        os.system(cmd)

    elif data == "open":
        cmd="""osascript -e 'tell application "iTunes" to activate'"""
        os.system(cmd)

    elif data == "close":
        cmd="""osascript -e 'tell application "iTunes" to quit'"""
        os.system(cmd)
    elif data == "0":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 0
            end tell'"""
            os.system(cmd)
    elif data == "1":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 1
            end tell'"""
            os.system(cmd)
    elif data == "2":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 2
            end tell'"""
            os.system(cmd)
    elif data == "3":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 3
            end tell'"""
            os.system(cmd)
    elif data == "4":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 4
            end tell'"""
            os.system(cmd)
    elif data == "5":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 5
            end tell'"""
            os.system(cmd)
    elif data == "6":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 6
            end tell'"""
            os.system(cmd)
    elif data == "7":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 7
            end tell'"""
    elif data == "8":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 8
            end tell'"""
            os.system(cmd)
    elif data == "9":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 9
            end tell'"""
            os.system(cmd)
    elif data == "10":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 10
            end tell'"""
            os.system(cmd)
    elif data == "11":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 11
            end tell'"""
            os.system(cmd)
    elif data == "12":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 12
            end tell'"""
            os.system(cmd)
    elif data == "13":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 13
            end tell'"""
            os.system(cmd)
    elif data == "14":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 14
            end tell'"""
            os.system(cmd)
    elif data == "15":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 15
            end tell'"""
            os.system(cmd)
    elif data == "16":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 16
            end tell'"""
            os.system(cmd)
    elif data == "17":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 17
            end tell'"""
            os.system(cmd)
    elif data == "18":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 18
            end tell'"""
            os.system(cmd)
    elif data == "19":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 19
            end tell'"""
            os.system(cmd)
    elif data == "20":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 20
            end tell'"""
            os.system(cmd)
    elif data == "21":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 21
            end tell'"""
            os.system(cmd)
    elif data == "22":
            print 'hola' 
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 22
            end tell'"""
            os.system(cmd)
    elif data == "23":
            print 'hola'
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 23
            end tell'"""
            os.system(cmd)
    elif data == "24":
            print 'hola' 
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 24
            end tell'"""
            os.system(cmd)
    elif data == "25":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 25
            end tell'"""
            os.system(cmd)
    elif data == "26":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 26
            end tell'"""
            os.system(cmd)
    elif data == "27":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 27
            end tell'"""
            os.system(cmd)
    elif data == "28":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 28
            end tell'"""
            os.system(cmd) 
    elif data == "28":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 29
            end tell'"""
            os.system(cmd) 
    elif data == "30":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 30
            end tell'"""
            os.system(cmd) 
    elif data == "31":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 31
            end tell'"""
            os.system(cmd) 
    elif data == "32":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 32
            end tell'"""
            os.system(cmd) 
    elif data == "33":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 33
            end tell'"""
            os.system(cmd) 
    elif data == "34":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 34
            end tell'"""
            os.system(cmd)
    elif data == "35":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 35
            end tell'"""
            os.system(cmd)
    elif data == "36":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 36
            end tell'"""
            os.system(cmd) 
    elif data == "37":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 37
            end tell'"""
            os.system(cmd) 
    elif data == "38":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 38
            end tell'"""
            os.system(cmd) 
    elif data == "39":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 39
            end tell'"""
            os.system(cmd) 
    elif data == "40":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 40
            end tell'"""
            os.system(cmd) 
    elif data == "41":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 41
            end tell'"""
            os.system(cmd) 
    elif data == "42":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 42
            end tell'"""
            os.system(cmd) 
    elif data == "43":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 43
            end tell'"""
            os.system(cmd) 
    elif data == "44":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 44
            end tell'"""
            os.system(cmd) 
    elif data == "45":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 45
            end tell'"""
            os.system(cmd) 
    elif data == "46":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 46
            end tell'"""
            os.system(cmd) 
    elif data == "47":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 47
            end tell'"""
            os.system(cmd) 
    elif data == "48":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 48
            end tell'"""
            os.system(cmd)
    elif data == "49":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 49
            end tell'"""
            os.system(cmd) 
    elif data == "50":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 50
            end tell'"""
            os.system(cmd) 
    elif data == "51":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 51
            end tell'"""
            os.system(cmd) 
    elif data == "52":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 52
            end tell'"""
            os.system(cmd) 
    elif data == "53":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 53
            end tell'"""
            os.system(cmd) 
    elif data == "54":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 54
            end tell'"""
            os.system(cmd) 
    elif data == "55":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 55
            end tell'"""
            os.system(cmd) 
    elif data == "56":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 56
            end tell'"""
            os.system(cmd) 
    elif data == "57":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 57
            end tell'"""
            os.system(cmd)
    elif data == "58":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 58
            end tell'"""
            os.system(cmd) 
    elif data == "59":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 59
            end tell'"""
            os.system(cmd) 
    elif data == "60":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 60
            end tell'"""
            os.system(cmd) 
    elif data == "61":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 61
            end tell'"""
            os.system(cmd)
    elif data == "62":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 62
            end tell'"""
            os.system(cmd)
    elif data == "63":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 63
            end tell'"""
            os.system(cmd)
    elif data == "64":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 64
            end tell'"""
            os.system(cmd)
    elif data == "65":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 65
            end tell'"""
            os.system(cmd)
    elif data == "66":
        cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 66
            end tell'"""
        os.system(cmd)
    elif data == "67":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 67
            end tell'"""
            os.system(cmd)
    elif data == "68":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 68
            end tell'"""
            os.system(cmd)
    elif data == "69":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 69
            end tell'"""
            os.system(cmd)
    elif data == "70":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 70
            end tell'"""
            os.system(cmd)
    elif data == "71":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 71
            end tell'"""
            os.system(cmd)
    elif data == "72":
        cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 72
            end tell'"""
        os.system(cmd)
    elif data == "73":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 73
            end tell'"""
            os.system(cmd)
    elif data == "74":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 74
            end tell'"""
            os.system(cmd)
    elif data == "75":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 75
            end tell'"""
            os.system(cmd)
    elif data == "76":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 76
            end tell'"""
            os.system(cmd)
    elif data == "77":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 77
            end tell'"""
            os.system(cmd)
    elif data == "78":
        cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 78
            end tell'"""
        os.system(cmd)
    elif data == "79":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 79
            end tell'"""
            os.system(cmd)
    elif data == "80":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 80
            end tell'"""
            os.system(cmd)
    elif data == "81":
        cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 81
            end tell'"""
        os.system(cmd)
    elif data == "82":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 82
            end tell'"""
            os.system(cmd)
    elif data == "83":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 83
            end tell'"""
            os.system(cmd)
    elif data == "84":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 84
            end tell'"""
            os.system(cmd)
    elif data == "85":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 85
            end tell'"""
            os.system(cmd)
    elif data == "86":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 86
            end tell'"""
            os.system(cmd)
    elif data == "87":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 87
            end tell'"""
            os.system(cmd)
    elif data == "88":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 88
            end tell'"""
            os.system(cmd)
    elif data == "89":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 89
            end tell'"""
            os.system(cmd)
    elif data == "90":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 90
            end tell'"""
            os.system(cmd)
    elif data == "91":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 91
            end tell'"""
            os.system(cmd)
    elif data == "92":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 92
            end tell'"""
            os.system(cmd)
    elif data == "93":
        cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 93
            end tell'"""
        os.system(cmd)
    elif data == "94":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 94
            end tell'"""
            os.system(cmd)
    elif data == "95":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 95
            end tell'"""
            os.system(cmd)
    elif data == "96":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 96
            end tell'"""
            os.system(cmd)
    elif data == "97":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 97
            end tell'"""
            os.system(cmd)
    elif data == "98":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 98
            end tell'"""
            os.system(cmd)
    elif data == "99":
            cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 99
            end tell'"""
            os.system(cmd)
    elif data == "100":
        cmd="""osascript -e 'tell application "iTunes"
            set the sound volume to 100
            end tell'"""
        os.system(cmd)
    elif data == "Exit":
        break
    

        
    	
    	

clie.close()
serv.close()
