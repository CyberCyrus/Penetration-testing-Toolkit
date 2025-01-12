import socket

def banner_grab(target, port):
    try:
        with socket.socket() as s:
            s.settimeout(2)
            s.connect((target, port))
            banner = s.recv(1024).decode().strip()
            return banner
    except:
        return "No banner retrieved"

if __name__ == "__main__":
    target = input("Enter target IP: ")
    port = int(input("Enter port to grab banner: "))
    banner = banner_grab(target, port)
    print(f"Banner: {banner}")
