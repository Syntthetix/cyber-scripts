import sys
import socket
import subprocess
from datetime import datetime

print("-" * 43)
print(" " * 15 + "BANNER GRABBER")
print("-" * 43)

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
if result.returncode == 0:
    print(result.stdout)
else:
    print(result.stderr)