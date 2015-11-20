import math

from pythonosc import dispatcher
from pythonosc import osc_server

class Server:

    def __init__(self, filter, sender):
        server = osc_server.ThreadingOSCUDPServer(
            (args.ip, args.port), dispatcher)
        print("Serving on {}".format(server.server_address))
        server.serve_forever()

        dispatcher = dispatcher.Dispatcher()
        dispatcher.map("/", print)
        dispatcher.map("/w", print_handler, "in")

    def print_handler(unused_addr, args, volume):
        print("{0}: {1}".format(args[0], volume))
