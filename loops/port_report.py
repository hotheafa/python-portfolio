# port_report.py
# Description: Categorizes and reports network ports into IANA port ranges (System, User, Dynamic).

start_port = int(input("Start port: "))
end_port = int(input("End port: ")) + 1
port_count = 0

for port in range(start_port,end_port ):
    
    if 0 < port <= 1023:
        print(f"{port}: system")
        port_count += 1
    elif 1024 <= port <= 49151:
        print(f"{port}: user")
        port_count += 1
    elif 49151 < port < 65535:
        print(f"{port}: dynamic")
        port_count += 1

print(f"Ports checked: {port_count}")

