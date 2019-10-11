import socket
import subprocess
import platform
import sys
import threading
from sys import stdout
if platform.system() == 'Windows':
    subprocess.call('cls', shell=True)
else:
    subprocess.call('clear', shell=True)
remoteServer  = input("Enter a remote host to scan: ")
if remoteServer.startswith('www') or remoteServer.startswith('http'):
    remoteServerIP  = socket.gethostbyname(remoteServer)
    print("-"*60)
    print("Received a web address")
else:
    remoteServerIP=remoteServer
    print("-"*60)
    print("Received an IP address")
print("-"*60)
print ("Please wait, scanning remote host", remoteServerIP)
def thread1(remoteserverIP):
    try:
        for port in range(1,16383):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteserverIP, port))
            stdout.write("\r Current Port: %d" % port)
            stdout.flush()
            if result == 0:
                print("\n")
                print("-"*60)
                print ("Port {}: 	 Open".format(port))
            sock.close()
    except socket.gaierror:
        print("-"*60)
        print ("Oops! Hostname could not be resolved. Exiting")
        sys.exit()
    except KeyboardInterrupt:
        print("-"*60)
        print("Really? Closing..... ")
        sys.exit()
    except socket.error:
        print("-"*60)
        print ("Oops! Couldn't connect to server")
        sys.exit()
def thread2(remoteserverIP):
    try:
        for port in range(16384,32766):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteserverIP, port))
            stdout.write("\r Current Port: %d" % port)
            stdout.flush()
            if result == 0:
                print("-"*60)
                print ("Port {}: 	 Open".format(port))
            sock.close()
    except socket.gaierror:
        print("-"*60)
        print ("Oops! Hostname could not be resolved. Exiting")
        sys.exit()
    except KeyboardInterrupt:
        print("-"*60)
        print("Really? Closing..... ")
        sys.exit()
    except socket.error:
        print("-"*60)
        print ("Oops! Couldn't connect to server")
        sys.exit()
def thread3(remoteserverIP):
    try:
        for port in range(32767,49149):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteserverIP, port))
            stdout.write("\r Current Port: %d" % port)
            stdout.flush()
            if result == 0:
                print("-"*60)
                print ("Port {}: 	 Open".format(port))
            sock.close()
    except socket.gaierror:
        print("-"*60)
        print ("Oops! Hostname could not be resolved. Exiting")
        sys.exit()
    except KeyboardInterrupt:
        print("-"*60)
        print("Really? Closing..... ")
        sys.exit()
    except socket.error:
        print("-"*60)
        print ("Oops! Couldn't connect to server")
        sys.exit()
def thread4(remoteserverIP):
    try:
        for port in range(49150,65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteserverIP, port))
            stdout.write("\r Current Port: %d" % port)
            stdout.flush()
            if result == 0:
                print("-"*60)
                print ("Port {}: 	 Open".format(port))
            sock.close()
    except socket.gaierror:
        print("-"*60)
        print ("Oops! Hostname could not be resolved. Exiting")
        sys.exit()
    except KeyboardInterrupt:
        print("-"*60)
        print("Really? Closing..... ")
        sys.exit()
    except socket.error:
        print("-"*60)
        print ("Oops! Couldn't connect to server")
        sys.exit()
if __name__ == '__main__':
    t1=threading.Thread(target=thread1,args=(remoteServerIP, ))
    t2=threading.Thread(target=thread2, args=(remoteServerIP, ))
    t3=threading.Thread(target=thread3, args=(remoteServerIP, ))
    t4=threading.Thread(target=thread4, args=(remoteServerIP, ))
    t1.start()
    t2.start()
    t3.start()
    t4.start()




