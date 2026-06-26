# import subprocess for pinging IP addresses
import subprocess

# opens addresses.txt in read mode and labels it as ip_list, then strips \n off
with open("addresses.txt", "r") as ip_list:
    ip_addresses = [line.strip() for line in ip_list]

# for each line in ip_addresses, take the result and pings each IP
for ip in ip_addresses:
    result = subprocess.run(["ping", "-c", "1", "-W", "1", ip], capture_output=True)
    output = result.stdout.decode()
    
    if result.returncode == 0:
        time = output.split("time=")[1].split(" ms")[0]
        print(ip,"|","ONLINE","|","Ping:",time)
    else:
        print(ip,"|","OFFLINE","|","Ping: NA")
