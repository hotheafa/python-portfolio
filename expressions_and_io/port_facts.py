#port_facts.py
#ورقم اخر منفذ  IPV4 برنامج يحسب عدد المنافذ و عدد عناوين  
## Cited references: RFC 791 and RFC 9293

PORT_BITS = 16
IPV4_BITS =  32
total_port = 2**(PORT_BITS)
total_ipv4 = 2**(IPV4_BITS)
highest_port = total_port - 1 
print (f"Total Port = {total_port}\nTotal IPV4 = {total_ipv4}\nHighest Port = {highest_port}")

