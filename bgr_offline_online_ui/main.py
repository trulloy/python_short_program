import socket

try:
    # Try to connect to Google's DNS server
    socket.create_connection(("8.8.8.8", 53), timeout=5)
    print("Internet on..")
except OSError:
    print("Internet off..")