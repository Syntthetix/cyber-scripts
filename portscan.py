import sys
import socket
from datetime import datetime

print("-" * 20)
print("  RAT PORT SCANNER")
print("-" * 20)
print()

if len(sys.argv) != 4:
    print("Error: Missing arguments!")
    print("Usage: portscan.py [target] [start_port] [end_port]")
    sys.exit()

target = sys.argv[1]

print("Scanning target: " + target)
print("Scan started at: " + str(datetime.now()))