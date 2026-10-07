#variables_and_types.py
MAX_CONNECTIONS = 12
device_name,device_ip,service,open_port = "PC Hotheafa","192.0.2.12","HTTPS", 443
print ("Name Device:",device_name)
print ("IP Address",device_ip)
print ("service:",service)
print ("Port Open:",open_port)
print ("MAXCONNECTIONS:",MAX_CONNECTIONS)
open_port,service = 22,"HTTP"
print ("Updated service:",service,"on port",open_port)
