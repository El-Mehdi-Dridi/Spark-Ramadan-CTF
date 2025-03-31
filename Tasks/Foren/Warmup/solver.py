from scapy.all import *

packets = rdpcap("warmup.pcap")
sorted_packets = sorted([p for p in packets if UDP in p and Raw in p], key=lambda p: p.time)
flag = ''.join(chr(len(p[Raw])) for p in sorted_packets)
print(flag)
