# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")
# (Runtime Error))int() The error here is the failure to convert to a proper number
port = int(input("Port: "))
#(Semantic Error) admin The error here is writing the equality value and assigning a value to the comparison substitute, which is a logical error because it will always print
is_admin = role =="admin"
##(Syntax Error) The error here is only in writing the sign backwards
is_system_port = port <= 1023
# (Semantic Error) 443 port == 443 The error here is that we need to put
is_web_port = port == 80 or port == 443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")
