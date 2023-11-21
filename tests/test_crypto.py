import hashlib
import unittest
import pwcrypto

class Test_Password_Cryptography(unittest.TestCase):

    def setUp(self):
        self.password123_sha256_hash = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f" # Obtained from https://emn178.github.io/online-tools/sha256.html
        self.Password1Exclamation_sha256_hash = "1d707811988069ca760826861d6d63a10e8c3b7f171c4441a6472ea58c11711b" # Obtained from https://emn178.github.io/online-tools/sha256.html
        self.abcdefghijklmnopqrstuvwxyz_sha256_hash = "71c480df93d6ae2f1efad1447c66c9525e316218cf51fc8d9ed832f2daf18b73" # Obtained from https://emn178.github.io/online-tools/sha256.html
        self.password123 = "password123"

    def test_password123(self):
        expected_hash = hashlib.sha256("password123".encode()).hexdigest()
        actual_hash = pwcrypto.encrypt("password123")

        self.assertEqual(expected_hash, actual_hash)

    def test_abcdefghijklmnopqrstuvwxyz_sha256_hash(self):
        expected_hash = hashlib.sha256("abcdefghijklmnopqrstuvwxyz".encode()).hexdigest()
        actual_hash = pwcrypto.encrypt("abcdefghijklmnopqrstuvwxyz")

        self.assertEqual(expected_hash, actual_hash)

    def test_Password1Exclamation(self):
        expected_hash = hashlib.sha256("Password1!".encode()).hexdigest()
        actual_hash = pwcrypto.encrypt("Password1!")

        self.assertEqual(expected_hash, actual_hash)

    
if __name__ == "__main__":
    unittest.main() 