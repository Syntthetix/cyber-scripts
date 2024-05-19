import sys
import socket
from datetime import datetime
import random
import time

random_order_notice = "*** Random port order enabled ***"
random_interval_notice = "*** Random scan interval enabled ***"
random_order = False
random_interval = False

print("-" * 43)
print(" " * 18 + "PORT SCANNER")
print("-" * 43)

if len(sys.argv) == 1:
    print("Usage:")
    print("portscan.py [target] <start_port> <end_port>")
    print("portscan.py [target] [start_port] (Scans only one port)")
    print("portscan.py [target] (Scans all 65535 ports)")
    sys.exit()

print("[1] No randomization")
print("[2] Randomize port order")
print("[3] Randomize time between scans (1-10 sec. intervals)")
print("[4] Randomize both")
choice = input("Choice (Default 1): ")

if choice == "" or choice == "1":
    print("None")
elif choice == "2":
    random_order = True
elif choice == "3":
    random_interval = True
elif choice == "4":
    random_order = True
    random_interval = True
print("-" * 43)
print(f"{random_order} {random_interval}")

target = socket.gethostbyname(sys.argv[1])
start_port = 1
end_port = 65535

# Set start_port and end_port to user-defined values if provided
# If only target and start_port are provided, only scan that one port
# Otherwise, scan the provided range
if (len(sys.argv) == 3):
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[2])

if (len(sys.argv) == 4):
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    if (end_port > 65535):
        print("Error: end_port cannot be greater than 65535!")
        sys.exit()


# Generate port array
ports = []
for port in range(start_port, end_port + 1):
    ports.append(port)

# Randomize port order
if random_order:
    random.shuffle(ports)

start_time = datetime.now()
print("Scan target:\t" + target)
print("Target ports:\t{} -> {}".format(start_port, end_port))
print("Started at:\t" + str(start_time))

if random_order or random_interval: print()
if random_order: print(random_order_notice)
if random_interval: print(random_interval_notice)

print("-" * 43)

# Begin scanning
try:
    open_port_count = 0

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            print("Found open port: " + str(port))
            open_port_count += 1
        s.close()

        # Wait between 5 and 15 seconds before the next scan
        if random_interval:
            wait_time = random.randint(5, 15)
            time.sleep(wait_time)
    
    if open_port_count == 0:
        print("No open ports found!")
    print("-" * 43)

    end_time = datetime.now()
    print("Open ports:\t" + str(open_port_count))
    print("Completed at:\t" + str(end_time))
    print("Elapsed time:\t" + str(end_time - start_time))

except KeyboardInterrupt:
    print("\nExiting due to keyboard interrupt!")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved!")
    sys.exit()
except socket.error:
    print("\nServer not responding!")
    sys.exit()