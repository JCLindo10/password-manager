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

    def test_long_string(self):
        expected_hash = hashlib.sha256("This is a really long string that has been made in order to test the encryption of really long strings in the password manager project being implemented by Lee Ramey, Nick House, and Jake Lindo".encode()).hexdigest()
        actual_hash = pwcrypto.encrypt("This is a really long string that has been made in order to test the encryption of really long strings in the password manager project being implemented by Lee Ramey, Nick House, and Jake Lindo")

        self.assertEqual(expected_hash, actual_hash)

    def test_double_hash(self):
        pre_expected_hash = hashlib.sha256("Hello, World!".encode()).hexdigest()
        expected_hash = hashlib.sha256(pre_expected_hash.encode()).hexdigest()
        pre_actual_hash = pwcrypto.encrypt("Hello, World!")
        actual_hash = pwcrypto.encrypt(pre_actual_hash)

        self.assertEqual(expected_hash, actual_hash)

    
if __name__ == "__main__":
    unittest.main() 