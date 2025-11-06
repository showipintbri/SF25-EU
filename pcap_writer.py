from scapy.all import PcapWriter, IP, TCP, Raw
import time
import csv


now = time.time()

sequence = 1

writer = PcapWriter("out_append.pcap", append=True, sync=True)

with open('sorted.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if not row:              # skip completely empty rows
            continue
        time_offset = int(row[0])
        payload_size = 1460 - int(row[1])
        timestamp = now + time_offset
        payload = b"x" * payload_size
        pkt = IP(dst="203.0.113.10")/TCP(dport=8080, sport=40000, flags="PA", seq=sequence)/Raw(payload)
        pkt.time = time_offset
        writer.write(pkt)
        sequence += payload_size
writer.close()
