import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

def print_handler(unused_addr, args, volume):
  print("{0}: {1}".format(args[0], volume))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="192.168.1.109", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=9000, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/", print)
  dispatcher.map("/w", print_handler, "in")

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()