from scapy.all import *

print("Starting Network Sniffer...\n")

packet_count = 0

def packet_callback(packet):
    global packet_count
    packet_count += 1

    print("\n==============================")
    print(f"Packet Number : {packet_count}")

    # IP Details
    if packet.haslayer(IP):
        print(f"Source IP      : {packet[IP].src}")
        print(f"Destination IP : {packet[IP].dst}")

    # Protocol Detection
    if packet.haslayer(TCP):
        print("Protocol       : TCP")

    elif packet.haslayer(UDP):
        print("Protocol       : UDP")

    elif packet.haslayer(ICMP):
        print("Protocol       : ICMP")

    # Payload Data
    if packet.haslayer(Raw):
        try:
            payload = packet[Raw].load.decode(errors='ignore')
            print(f"Payload        : {payload[:100]}")
        except:
            pass

# Capture packets
packets = sniff(prn=packet_callback, count=20)

# Save packets to file
wrpcap("captured_packets.pcap", packets)

print("\nPackets saved to captured_packets.pcap")