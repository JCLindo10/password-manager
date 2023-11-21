import unittest
import pwcrypto

class Test_Password_Cryptography(unittest.TestCase):

    def setUp(self):
        self.password123_sha256_hash = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
        self.abcdefghijklmnopqrstuvwxyz_sha256_hash = "71c480df93d6ae2f1efad1447c66c9525e316218cf51fc8d9ed832f2daf18b73"

    def test_password123(self):
        self.assertEqual(self.password123_sha256_hash, pwcrypto.encrypt("password123"))

    def test_abcdefghijklmnopqrstuvwxyz_sha256_hash:
        self.assertEqual(self.abcdefghijklmnopqrstuvwxyz_sha256_hash, pwcrypto.encrypt("abcdefghijklmnopqrstuvwxyz"))

    
if __name__ == "__main__":
    unittest.main() 