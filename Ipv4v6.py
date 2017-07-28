#Class to check wether the ip is correct or not
import socket, sys

class Ipv4v6:

    def __init__(self,address):
        self.address = address

    def valid_ip(self):
	#check if an ip is valid or not
	try:
	    b1 = socket.inet_pton(socket.AF_INET6,self.address)
	    pass
	except:
	    try:
	        b2 = socket.inet_pton(socket.AF_INET,self.address)
	        pass
	    except:
                print("\033[1m\033[31mInvalid IP format !\033[0m \nYet, IPv6 and IPv4 handled.")
                sys.exit(1)
