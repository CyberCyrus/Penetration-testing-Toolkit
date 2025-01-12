import socket
from utils.report_generator import generate_report

def port_scan(target, ports):
    open_ports = []
    print(f"Scanning target {target}...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
    generate_report("Port Scanner", {"target": target, "open_ports": open_ports})
    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    ports_to_scan = range(1, 1025)
    open_ports = port_scan(target_ip, ports_to_scan)
    print(f"Open ports: {open_ports}")
