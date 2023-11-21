import hashlib
import unittest
import pwcrypto

class Test_Password_Cryptography(unittest.TestCase):

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

    def test_empty_string(self):
        expected_hash = hashlib.sha256("".encode()).hexdigest()
        actual_hash = pwcrypto.encrypt("")

        self.assertEqual(expected_hash, actual_hash)

    
if __name__ == "__main__":
    unittest.main() 