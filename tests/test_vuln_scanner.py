import unittest
from modules.vuln_scanner import check_vulnerability

class TestVulnerabilityScanner(unittest.TestCase):
    def test_known_vulnerabilities(self):
        service = "nginx"
        version = "1.18.0"
        vulns = check_vulnerability(service, version)
        self.assertIn("CVE-2020-1234", vulns)

    def test_no_vulnerabilities(self):
        service = "unknown_service"
        version = "0.0.0"
        vulns = check_vulnerability(service, version)
        self.assertEqual(vulns, [])

if __name__ == "__main__":
    unittest.main()
