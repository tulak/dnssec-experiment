from scapy.all import *
from IPython import embed

filter = "udp port 53"
def apply_packet(pkt):
  print pkt
  embed()
  return "OK"
sniff(filter=filter,prn=apply_packet)
