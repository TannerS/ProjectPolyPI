
import socket
import sys
import struct
import numpy as np
import json

HOST = '127.0.0.1'  # Symbolic name, meaning all available interfaces
PORT = 8089  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

# Bind socket to local host and port
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



# Receiving from client
# data = conn.recv(10000)


# values = bytearray(json_str, 'utf-8')
# values = bytes(json_str, 'utf-8')

# print("DEBUG: " + str(values))


# json_str2 = np.array(json.loads(json_str))

# print(json_str2)


# while True:
#     new_data = conn.recv(1)
#     if new_data:
#         json_str += str(new_data)
#     else:
#         json_str += str(new_data[:])
#         print ("no more data from" )
#         break
#
# print("DATA: "  +str(json_str[:-1]))
#


# print ("DEBUG -----" + str(data))

# unpacked_data = struct.unpack("s",values)

# unpacked_data = struct.unpack("=s",data)




# print("DEBUG: " + json.loads(data))



# print (json_str)


# unpacked_data = struct.unpack("",data)

#
# unpacked_data = struct.unpack("@s", data)
# unpacked_data2 = struct.unpack("=s", data)
# unpacked_data3= struct.unpack(">s", data)
#
#  # intel is little endian, java vm is big endian
# unpacked_data4  = struct.unpack("<s", data)
# unpacked_data5  = struct.unpack("!s", data)
# unpacked_data6  = struct.unpack("s", data)

# print("DATA3: " + str(unpacked_data))
# print("DATA5: " + str(unpacked_data2))
# print("DATA3: " + str(unpacked_data3))
# print("DATA5: " + str(unpacked_data4))
# print("DATA5: " + str(unpacked_data5))
# print("DATA5: " + str(unpacked_data6))






