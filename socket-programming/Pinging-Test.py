import subprocess
import ipaddress



try:

    ip = input("Enter in the IP you wish to ping: ")
    try:
        ipaddress.IPv4Address(ip)
    except ValueError as e:
        print(f"Error! Could not ping {ip} due to {e}")

    ping = subprocess.check_output([f"ping", "{ip}"])
    ping = ping.decode('utf-8').replace("\r", "")
    ping = ping.split()
    count = 0

    if len(ping) in [f"Reply from {ip}"]:
        count += 1
except subprocess.CalledProcessError as e:
    print(f"Error received! {e}")

if count == 4:
    print("Default Gateway successfully pinged!")
elif count == 3:
    print("3 out 4 packets received!")
elif count == 2:
    print("2 out 4 packets received!")
elif count == 1:
    print("1 out 4 packets received!")
else:
    print("Error! Cannot ping Default Gateway")
