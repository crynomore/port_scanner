import socket
import subprocess
import platform
from sys import stdout
if platform.system() == 'Windows':
    subprocess.call('cls', shell=True)
else:
    subprocess.call('clear', shell=True)
remoteServer  = input("Enter a remote host to scan: ")
if remoteServer.startswith('www') or remoteServer.startswith('http'):
    remoteServerIP  = socket.gethostbyname(remoteServer)
    print("\n")
    print("-"*60)
    print("Received a web address")
else:
    remoteServerIP=remoteServer
    print("\n")
    print("-"*60)
    print("Received an IP address")
print("\n")
print("-"*60)
print ("Please wait, scanning remote host", remoteServerIP)
try:
    for port in range(1,65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        stdout.write("\r Current Port: %d" % port)
        stdout.flush()
        if result == 0:
            print("\n")
            print("-"*60)
            print ("Port {}:     Open".format(port))
        sock.close()
except socket.gaierror:
    print("\n")
    print("-"*60)
    print ("Oops! Hostname could not be resolved. Exiting")
    sys.exit()
except KeyboardInterrupt:
    print("\n")
    print("-"*60)
    print("Really? Closing..... ")
    sys.exit()
except socket.error:
    print("\n")
    print("-"*60)
    print ("Oops! Couldn't connect to server")
    sys.exit()
