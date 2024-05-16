import sys
import socket
from datetime import datetime

print("-" * 20)
print("  RAT PORT SCANNER")
print("-" * 20)

if len(sys.argv) == 3:
    print("Error: Missing arguments!")
    print("Usage: portscan.py [target] [start_port] <end_port>")
    print("pyscan.py [target] (Defaults to all ports)")
    sys.exit()

if (len(sys.argv) == 4):
    start_port = sys.argv[2]
    end_port = sys.argv[3]

target = sys.argv[1]
start_port = 1
end_port = 65535

print("Scan target:\t" + target)
print("Target ports:\t{} -> {}".format(start_port, end_port))
print("Started at:\t" + str(datetime.now()))