import socket
import sys
import argparse
import re
import time

script_name = sys.argv[0]

arguments = argparse.ArgumentParser(description="Port Scanning tool", usage=f"python3 {script_name} -t Target IP -p Target Port(s)")
arguments.add_argument('-t', "--target", help="Enter the Target IP to scan Ports", required=True)
arguments.add_argument('-p', "--port", help="Enter the Target Port(s) e.g 21 | 22,23,21 | 1-65535", required=True)
args = arguments.parse_args()

target_ip = args.target
port = args.port

port_list = re.split('[,-]', port)

current_time = time.ctime()
print(f"[*] Scanning Started at {current_time}\n")

start_time = time.time()

if "-" in port:
    for ports in range(int(port_list[0]), int(port_list[1]) + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        connection = s.connect_ex((target_ip, ports))
        if connection == 0:
            print(f"[+] Port {ports} is open on {target_ip}")
else:
    for str_ports in port_list:
        int_ports = int(str_ports)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        connection = s.connect_ex((target_ip, int_ports))
        if connection == 0:
            print(f"[+] Port {int_ports} is open on {target_ip}")


end_time = time.time()
execution_time = end_time - start_time
print("\n[*] Total time took for Scanning {:.2f} seconds".format(execution_time))
