"""
This program sends 10 random values between 0.0 and 1.0,
waiting for 200 milliseconds between each value.
"""
TARGET_IP = "192.168.1.107"
TARGET_PORT = 9000

from time import sleep
from sender import sender
from random import random

def main():


	send = sender.Sender(TARGET_IP, TARGET_PORT)

	while 1:
		send.sendValue("/w", random() * 100)
		sleep(0.2)
		

if __name__ == "__main__":
    main()
