
import socket
import sys
import struct
import numpy as np
import json

HOST = ''
PORT = 8106

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ('Socket bind complete')


s.listen(10)


print ('Socket now listening')
conn, addr = s.accept()
print ('Connected with ' + addr[0] + ':' + str(addr[1]))




json_str = ""





while True:
    # Receiving from client
    print("get data")
    data = conn.recv(1024)
    temp =  data.decode()
    # json_str += data.decode()
    json_str += temp
    print(json_str)
    if not data:
        break


print("DEBUG: " + str(json_str))

conn.close()
s.close()

json_str = json_str.strip('\n')

json_arr = np.array(json.loads(json_str))

print("DEBUG: " + str(json_arr))






