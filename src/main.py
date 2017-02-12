
import socket
import sys
import struct
import numpy as np
import json
#import RPi.GPIO as GPIO
#import time # used for time.sleep()

#GPIO.setmode(GPIO.BCM)
HOST = ''

PORT = 8120

pins = [14,15,18,23,24,25,8,7]

for y in range(len(pins)):
    GPIO.setup(pins[y], GPIO.OUT)
    print("setting pin: " + pins[y])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ('Socket bind complete')


s.listen(1)


print ('Socket now listening')
conn, addr = s.accept()
print ('Connected with ' + addr[0] + ':' + str(addr[1]))




json_str = ""



while True:
    # Receiving from client
    print("get data")



    data = conn.recv(1026)
    temp =  data.decode()
    # print("TEST: " + temp)
    # json_str += data.decode()
    json_str += temp
    # print(json_str)

    json_str = json_str.strip('\n')

    json_arr = np.array(json.loads(json_str))

    print(str(json_arr))

    json_str = ""

    if not data:
        break



conn.close()
s.close()



def sendDataToGpio():
    print("hi")
