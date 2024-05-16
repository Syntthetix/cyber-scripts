import sys
import socket
from datetime import datetime

print("-" * 43)
print(" " * 14 + "RAT PORT SCANNER")
print("-" * 43)

if len(sys.argv) == 3:
    print("Error: Missing arguments!")
    print("Usage: portscan.py [target] [start_port] <end_port>")
    print("pyscan.py [target] (Defaults to all ports)")
    sys.exit()

target = sys.argv[1]
start_port = 1
end_port = 65535

# Set start_port and end_port to user-defined values if provided
if (len(sys.argv) == 4):
    start_port = sys.argv[2]
    end_port = sys.argv[3]
    if (int(end_port) > 65535):
        print("Error: end_port cannot be greater than 65535!")
        sys.exit()

print("Scan target:\t" + target)
print("Target ports:\t{} -> {}".format(start_port, end_port))
print("Started at:\t" + str(datetime.now()))
print("-" * 43)

# Begin scanning