# import subprocess for pinging IP addresses and os for reading ~ as $HOME and datetime
import subprocess
import os
from datetime import datetime

file_location = input("Location of your IP address list:")

# opens addresses.txt in read mode and labels it as ip_list, then strips \n off
with open(os.path.expanduser(file_location), "r") as ip_list:
    ip_addresses = [line.strip() for line in ip_list]

# create directory if it doesn't exist yet
os.makedirs("reports", exist_ok=True)

report_output = []

# for each line in ip_addresses, take the result and pings each IP
for ip in ip_addresses:
    if os.name == "posix":
        flags = ["-c", "1", "-W", "1"]
    elif os.name == "nt":
        flags = ["-n", "1", "-w", "1000"]
    else:
        print("Unsupported operating system")
        exit()

    result = subprocess.run(["ping"] + flags + [ip], capture_output=True)
    output = result.stdout.decode()
   
   # checks if output from ping command was a success or failure
    if result.returncode == 0:
        # if it was a success then take just the ping time in ms
        time = output.split("time=")[1].split(" ms")[0]
        line = ip + " | ONLINE | Ping(ms): " + time + "\n"
        print(line)
        report_output.append(line)
    else:
        line = ip + " | OFFLINE" + "\n"
        print(line)
        report_output.append(line)



save_answer = input("Would you like to save this report? (y/n): ")


# save file
if save_answer in ["y", "yes", "Yes", "Y"]:
    subprocess.run("clear")
    date = datetime.now().strftime("%Y-%m-%d")
    name_append = input("What would you like to call this file?")
    filename = date + " - " + name_append + ".txt"
    save_location = "reports/" + filename
    
    with open(save_location, "w") as report:
        report.writelines(report_output)

else:
    exit()
