from pythonosc import osc_message_builder
from pythonosc import udp_client

class Sender:
	
	def __init__(self, TargetIp, TargetPort):
		self.ip = TargetIp
		self.port = TargetPort

		self.sender = udp_client.UDPClient(self.ip, self.port)


	def sendValue(self, Address, Value):
		print("sending %s to '%s'" % (Value, Address))
		msg = osc_message_builder.OscMessageBuilder(address = Address)
		msg.add_arg(Value)
		msg = msg.build()
		self.sender.send(msg)