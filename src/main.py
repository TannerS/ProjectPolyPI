
import socket
import sys
import struct
import numpy as np
import json

HOST = ''
PORT = 8089

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
    data = conn.recv(1024)
    print ( str(type(data)))
    json_str += data.decode()
    if not data:
        break


print("DEBUG: " + str(json_str))

conn.close()
s.close()

json_str = json_str.strip('\n')

json_arr = np.array(json.loads(json_str))

print("DEBUG: " + str(json_arr))






