import unittest
from modules.banner_grabber import banner_grab

class TestBannerGrabber(unittest.TestCase):
    def test_banner_grab_no_service(self):
        target = "127.0.0.1"
        port = 12345  # Port unlikely to have a service
        banner = banner_grab(target, port)
        self.assertEqual(banner, "No banner retrieved")  # No banner expected

if __name__ == "__main__":
    unittest.main()
