import unittest
import pwcrypto

class Test_Password_Cryptography(unittest.TestCase):

    def setUp(self):
        self.password123_sha256_hash = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
        self.abcdefghijklmnopqrstuvwxyz_sha256_hash = "71c480df93d6ae2f1efad1447c66c9525e316218cf51fc8d9ed832f2daf18b73"
        self.Password1Exclamation_sha256_hash = "1d707811988069ca760826861d6d63a10e8c3b7f171c4441a6472ea58c11711b"

    def test_password123(self):
        self.assertEqual(self.password123_sha256_hash, pwcrypto.encrypt("password123"))

    def test_abcdefghijklmnopqrstuvwxyz_sha256_hash(self):
        self.assertEqual(self.abcdefghijklmnopqrstuvwxyz_sha256_hash, pwcrypto.encrypt("abcdefghijklmnopqrstuvwxyz"))

    def test_Password1Exclamation(self):
        self.assertEqual(self.Password1Exclamation_sha256_hash, pwcrypto.encrypt("Password1!"))

    
if __name__ == "__main__":
    unittest.main() 