import requests

def check_vulnerability(service, version):
    # Dummy implementation for demonstration
    vulnerabilities = {
        "nginx/1.18.0": ["CVE-2020-1234"],
        "apache/2.4.41": ["CVE-2019-6789"],
    }
    return vulnerabilities.get(f"{service}/{version}", [])

if __name__ == "__main__":
    service = input("Enter service name: ")
    version = input("Enter service version: ")
    vulns = check_vulnerability(service, version)
    if vulns:
        print(f"Vulnerabilities found: {vulns}")
    else:
        print("No known vulnerabilities found.")
