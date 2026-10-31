import socket
import sys

if len(sys.argv) != 2:
    print("Usage: python3 resolver.py <hostname>")
    sys.exit(1)

hostname = sys.argv[1]
try:
    ip_address = socket.gethostbyname(hostname)

except socket.gaierror:
    print(f"Error: could not resolve hostname '{hostname}'")
    sys.exit(1)

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
