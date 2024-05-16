import sys
import socket
from datetime import datetime

print("-" * 20)
print("  RAT PORT SCANNER")
print("-" * 20)
print()

target = sys.argv[1]

print("Scanning target: " + target)
print("Scan started at: " + str(datetime.now()))