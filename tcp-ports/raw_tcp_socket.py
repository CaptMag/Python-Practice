import socket

def Calculate_Checksum():
    

def raw_packet():

    # destination = input("Enter a domain or IPv4 Address: ")

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    ip_header = b'\x45\x00\x00\x34' # Version, IHL, TOS, Total Length
    ip_header += b'\x49\x1f\x40\x00' # Identification, Flags, Fragment Offset
    ip_header += b'\x80\x06\xa1\xa1' # TTL, Protocol, Header Checksum
    ip_header += b'\xc0\xa8\x01\x9e' # Source IP Address (192.168.1.158)
    ip_header += b'\x2d\x21\x20\x9c' # Destination IP Address (45.33.32.156)

    pseudo_header = b'\xc0\xa8\x01\x9e'  # source IP
    pseudo_header += b'\x2d\x21\x20\x9c' # destination IP
    pseudo_header += b'\x00'            # reserved
    pseudo_header += b'\x06'            # protocol
    pseudo_header += b'\x00\x14'        # TCP length (20 bytes)

    tcp_header = b'\xa8\xe2\x00\x50' # Source and Destination Port
    tcp_header += b'\x0f\xfd\x79\x76' # Sequence Number
    tcp_header += B'\x00\x00\x00\x00' # ACK Number
    tcp_header += b'\x80\x02\xfa\xf0' # SYN Flag, FIN Flag, Window Size
    tcp_header += tcp_checksum.to_bytes(2, 'big') + b'\x00\x00' # Checksum, Urgent Pointer

    checksum_data = pseudo_header + tcp_header
    tcp_checksum = raw_packet(checksum_data)
    packet = ip_header + tcp_header
    try:
        s.sendto(packet, ('45.33.32.156', 80))
    except socket.gaierror as e:
        print(f"Could not connect to port 80! reason {e}")

if __name__ == "__main__":
    raw_packet()
