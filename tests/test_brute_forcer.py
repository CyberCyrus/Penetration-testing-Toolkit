import unittest
from modules.brute_forcer import ssh_brute_force

class TestBruteForcer(unittest.TestCase):
    def test_invalid_credentials(self):
        target = "127.0.0.1"
        username = "fake_user"
        password_list = ["wrong_password"]
        result = ssh_brute_force(target, username, password_list)
        self.assertIsNone(result)  # No password should match

if __name__ == "__main__":
    unittest.main()
