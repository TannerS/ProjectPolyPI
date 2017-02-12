import socket
import sys
import struct
import numpy as np
import json

#import RPi.GPIO as GPIO
#import time # used for time.sleep()

#GPIO.setmode(GPIO.BCM)
from src.Matrix import Matrix

HOST = ''

PORT = 8128

pins = [14,15,18,23,24,25,8,7]

# for y in range(len(pins)):
    # GPIO.setup(pins[y], GPIO.OUT)
    # print("setting pin: " + pins[y])

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
matrix = [[0 for x in range(8)] for y in range(8)]

data_reader = Matrix(matrix)
data_reader.start()

print("Debug")

while True:
    data = conn.recv(1026)
    temp =  data.decode()
    json_str += temp
    json_str = json_str.strip('\n')
    json_arr = np.array(json.loads(json_str))
    matrix = json_arr
    print(str(json_arr))
    data_reader.setData(json_arr)
    json_str = ""

    if not data:
        break

conn.close()
s.close()



def sendDataToGpio():
    print("hi")
