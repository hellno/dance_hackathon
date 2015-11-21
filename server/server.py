import math
import socket
import sys

from pythonosc import dispatcher
from pythonosc import osc_server

class Server:

    def osc_handler(self, unused_addr, args, val):
        print("{0}: {1}".format(args[0], val))
        
        try:
            self.f.put(float(data.rstrip()))
        except ValueError:
            print("Cannot_ConvertLatestDataPacket")
        else:
            self.class_nr  = self.f.latest_class(4)
            
            if(class_nr):    
                print("latest class is %d " % (self.class_nr))
                self.sender.sendValue("/w", self.class_nr)


    def __init__(self, filter, sender, ip, port):
        self.filter = filter
        self.sender = sender
        self.ip = ip
        self.port = port

        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.map("/", print)
        self.dispatcher.map("/w", self.osc_handler, "in")

        self.server = osc_server.ThreadingOSCUDPServer(
            (self.ip, self.port), self.dispatcher)
        print("Serving on {}".format(self.server.server_address))
        self.server.serve_forever()

        
        
