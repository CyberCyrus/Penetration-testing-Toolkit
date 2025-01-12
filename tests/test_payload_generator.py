import unittest
from modules.payload_generator import generate_payload

class TestPayloadGenerator(unittest.TestCase):
    def test_reverse_shell_payload(self):
        payload = generate_payload("reverse_shell")
        self.assertIn("/dev/tcp", payload)

    def test_buffer_overflow_payload(self):
        payload = generate_payload("buffer_overflow")
        self.assertEqual(len(payload), 1024)

    def test_unknown_payload(self):
        payload = generate_payload("unknown_type")
        self.assertEqual(payload, "Unknown payload type")

if __name__ == "__main__":
    unittest.main()
