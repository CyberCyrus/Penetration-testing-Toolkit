from modules.port_scanner import port_scan
from modules.brute_forcer import ssh_brute_force
from modules.banner_grabber import banner_grab
from modules.vuln_scanner import check_vulnerability
from modules.payload_generator import generate_payload

def main():
    print("Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. SSH Brute-Forcer")
    print("3. Banner Grabber")
    print("4. Vulnerability Scanner")
    print("5. Payload Generator")
    choice = input("Choose a module: ")
    if choice == "1":
        target = input("Enter target IP: ")
        ports = range(1, 1025)
        print(f"Open ports: {port_scan(target, ports)}")
    elif choice == "2":
        target = input("Enter target IP: ")
        username = input("Enter username: ")
        password_file = input("Enter path to password file: ")
        with open(password_file) as f:
            passwords = f.read().splitlines()
        ssh_brute_force(target, username, passwords)
    elif choice == "3":
        target = input("Enter target IP: ")
        port = int(input("Enter port: "))
        print(f"Banner: {banner_grab(target, port)}")
    elif choice == "4":
        service = input("Enter service: ")
        version = input("Enter version: ")
        print(f"Vulnerabilities: {check_vulnerability(service, version)}")
    elif choice == "5":
        payload_type = input("Enter payload type: ")
        print(f"Generated payload: {generate_payload(payload_type)}")

if __name__ == "__main__":
    main()
