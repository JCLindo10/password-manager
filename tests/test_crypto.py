import unittest
import pwcrypto

class Test_Password_Cryptography(unittest.TestCase):

    def setUp(self):
        self.password123_sha256_hash = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"

    def test_password123(self):
        self.assertEqual(self.password123_sha256_hash, pwcrypto.encrypt("password123"))
    
if __name__ == "__main__":
    unittest.main() 