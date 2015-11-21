from filter import filter
from sender import sender
from server import server

RECEIVING_IP = '' # can be empty -> localhost
RECEIVING_PORT = 4444
 
TARGET_IP = "192.168.1.105"
TARGET_PORT = 9000

RANGE_MIN = 0
RANGE_MAX = 100

filt = filter.Filter(RANGE_MIN, RANGE_MAX)
send = sender.Sender(TARGET_IP, TARGET_PORT)
serv = server.Server(filt, send, RECEIVING_IP, RECEIVING_PORT)
while 1:
    try:
        pass
    except KeyboardInterrupt:
        print("tried to quit!")
        serv.shutdown()