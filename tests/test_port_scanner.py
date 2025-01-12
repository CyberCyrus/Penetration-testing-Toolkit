import unittest
from modules.port_scanner import port_scan

class TestPortScanner(unittest.TestCase):
    def test_scan_known_open_ports(self):
        # Test localhost for common open ports
        target = "127.0.0.1"
        ports = [22, 80, 443]
        result = port_scan(target, ports)
        self.assertIsInstance(result, list)  # Ensure result is a list

    def test_scan_no_open_ports(self):
        target = "127.0.0.1"
        ports = [9999]  # Unlikely port to be open
        result = port_scan(target, ports)
        self.assertEqual(result, [])  # No open ports expected

if __name__ == "__main__":
    unittest.main()
