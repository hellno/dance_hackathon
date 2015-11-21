from filter import filter
from sender import sender
from server import server

RECEIVING_IP = '' # can be empty -> localhost
RECEIVING_PORT = 4444
 
TARGET_IP = "192.168.1.105"
TARGET_PORT = 9000

f = filter.Filter()
s = sender.Sender(TARGET_IP, TARGET_PORT)
server = server.Server(f, s, RECEIVING_IP, RECEIVING_PORT)