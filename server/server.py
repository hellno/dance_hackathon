import math
import socket
import sys

from pythonosc import dispatcher
from pythonosc import osc_server

class Server:

    def osc_handler(self, unused_addr, args, val):
        # print("{0}: {1}".format(args[0], val))
        
        try:
            self.filter.put(float(val))
        except ValueError:
            print("Cannot_ConvertLatestDataPacket")
        else:
            self.class_nr  = self.filter.latest_class(4)
            
            if(self.class_nr):    
                print("class is %d " % (self.class_nr))
                self.log.write("%d\n" % (self.class_nr))
                self.log.flush()
                
                self.sender.sendValue("/w", self.class_nr)


    def __init__(self, filter, sender, ip, port):
        self.filter = filter
        self.sender = sender
        self.ip = ip
        self.port = port
        self.class_nr = -1

        self.log = open('log.txt', 'w', 3)

        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.map("/", print)
        self.dispatcher.map("/w", self.osc_handler, "in")

        self.server = osc_server.ThreadingOSCUDPServer(
            (self.ip, self.port), self.dispatcher)
        print("Listening on {}".format(self.server.server_address))
        self.server.serve_forever()

    def shutdown(self):
        self.log.close()

        
        
