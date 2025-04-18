import subprocess
import ipaddress
import sys



try:
        # User must enter valid IPv4 address
    ip = input("Enter in the IP you wish to ping: ")


    try:
        ipaddress.IPv4Address(ip)
    except ValueError as e:
        print(f"Error! Could not ping {ip} due to {e}")
        sys.exit(1) # Code will exit if unsuccessful

    print("\n Pinging desired IP... \n")

    ping = subprocess.check_output(["ping", ip]) # Pings desired IP and then checks its output


    ping = ping.decode('utf-8').replace("\r", "") # Converts raw binary data into human-readable strings

    count = 0
    ping_lines = ping.splitlines() # Splits the output into seperate lines
    for line in ping_lines: # Goes into a loop to ensure pings are either successful or not


        if "Reply from" in line and ip in line: # if "reply from" is found in a string, it is counted
            count += 1
                
except subprocess.CalledProcessError as e:
    print(f"Error received! {e}")

if count == 4:
    print(f"4 out of 4 packets received! {ip} successfully pinged!")
elif count == 3:
    print("3 out 4 packets received!")
elif count == 2:
    print("2 out 4 packets received!")
elif count == 1:
    print("1 out 4 packets received!")
else:
    print("Error! Cannot ping Default Gateway")
