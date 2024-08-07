import socket
from scapy.all import *
from scapy.layers.l2 import Ether

sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

interface = "eth0"
sniffer.bind((interface, 0))

try:
    while True:
        raw_data, addr = sniffer.recvfrom(65535)
        packet = Ether(raw_data)
        print(packet.summary())

except KeyboardInterrupt:
    sniffer.close()