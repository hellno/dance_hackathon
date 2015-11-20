import socket
import sys
from filter import filter
from sender import sender
from server import server

HOST = ''
PORT = 4444
 
TARGET_IP = "192.168.1.107"
TARGET_PORT = 9000

f = filter.Filter()
send = sender.Sender(TARGET_IP, TARGET_PORT)
server = server.Server(f, s)

while 1:
    #receive message
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break

    print("received %s" % data.rstrip())
    
    try:
        f.put(float(data.rstrip()))
    except ValueError:
        print("Cannot_ConvertLatestDataPacket")
    else:
        class_nr  = f.latest_class(4)
        
        if(class_nr):    
            print("latest class is %d " % (class_nr))
            send.sendValue("/w", class_nr)

#### OLD UDP CLIENT ####
# setup of UDP CLIENT
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')
except(socket.error, msg):
    print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
 
try:
    s.bind((HOST, PORT))
except(socket.error , msg):
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print('Socket bind complete')
# end of setup of UDP CLIENT
s.close()