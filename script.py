# import subprocess for pinging IP addresses and os for reading ~ as $HOME
import subprocess
import os

file_location = input("Location of your IP address list:")

# opens addresses.txt in read mode and labels it as ip_list, then strips \n off
with open(os.path.expanduser(file_location), "r") as ip_list:
    ip_addresses = [line.strip() for line in ip_list]

# for each line in ip_addresses, take the result and pings each IP
for ip in ip_addresses:
    result = subprocess.run(["ping", "-c", "1", "-W", "1", ip], capture_output=True)
    output = result.stdout.decode()
   
   # checks if output from ping command was a success or failure
    if result.returncode == 0:
        # if it was a success then take just the ping time in ms
        time = output.split("time=")[1].split(" ms")[0]
        print(ip, "|", "ONLINE", "|", "Ping:", time)
    else:
        print(ip, "|", "OFFLINE", "|", "Ping: N/A")
