import socket
from struct import *

def create_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error as e:
        print(f"Socket could not be established. Reason: {e}")

def ip_header():
    source_ip = '192.168.1.158'
    destination_ip = socket.gethostbyname('scanme.nmap.org')

    # IP Header fields 
    ip_ver = 4
    ip_ihl = 5
    ip_tos = 0
    ip_frag_off = 0
    ip_len = 52
    ip_id = 11944
    ip_ttl = 128
    ip_proto = socket.IPPROTO_TCP
    ip_check = 0
    ip_saddr = socket.inet_aton(source_ip)
    ip_daddr = socket.inet_aton(destination_ip)

    ip_ihl_ver = (ip_ver << 4) + ip_ihl
    ip_header = pack('!BBHHHBBH4s4s' , ip_ihl_ver, ip_tos, ip_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)

    tcp_header(source_ip, destination_ip)

def tcp_header(source_ip, destination_ip):

    user_data = 'hello, how are you'

    # TCP Header Fields
    tcp_source = 24902
    tcp_dest = 80
    tcp_seq = 0
    tcp_ack_seq = 0
    tcp_doff = 5

    # Flags

    tcp_fin = 0
    tcp_syn = 1
    tcp_rst = 0
    tcp_psh = 0
    tcp_ack = 0
    tcp_urg = 0
    tcp_window = 64240
    tcp_checksum = 0
    tcp_urgent_pointer = 0

    tcp_offset_res = (tcp_doff << 4) + 0
    tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + (tcp_psh <<3) + (tcp_ack << 4) + (tcp_urg << 5)
    tcp_header = pack('!HHLLBBHHH' , tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags,  tcp_window, tcp_checksum, tcp_urgent_pointer)

    # Pseudo Header Fields
    pseudo_sport = socket.inet_aton(source_ip)
    pseudo_dport = socket.inet_aton(destination_ip)
    pseudo_reserved = 0
    pseudo_protocol = socket.IPPROTO_TCP
    pseudo_tcp_length = 20

    psh = pack('!4s4sBBH')
