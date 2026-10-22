#port_classifier.py
# A program to verify and classify port numbers according to IANA ranges and specified services.

port = int(input("Port: "))
if port < 0 or port > 65535:
    print("Invalid port: use a number from 0 to 65535.")
#Domain classification (for valid ports) so that the domain to which the port belongs is printed
else:
    if port <= 1023:
       print("Range: system")
    elif port <= 49151:
       print("Range: user")
    else:
       print("Range: dynamic or private")
#Service restricted to ports 22, 80 and 443 only
if port == 22:
    print("Service: ssh")
if port == 80:
    print("Service: http")
if port == 443:
    print("Service: https")
