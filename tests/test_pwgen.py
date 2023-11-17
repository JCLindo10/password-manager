import unittest
import pwgen

class Test_Password_Generation(unittest.TestCase):


    def setUp(self):
        self.test_depth = 10
        self.len_passwords = [""] * self.test_depth
        for num in range(self.test_depth):
            self.len_passwords[num] = pwgen.gen(num)
        
        self.special_passwords = [""] * self.test_depth
        for num in range(self.test_depth):
            self.special_passwords[num] = pwgen.gen(self.test_depth, special_chars=True)

        self.num_passwords = [""] * self.test_depth
        for num in range(self.test_depth):
            self.num_passwords[num] = pwgen.gen(self.test_depth, numbers=True)

        self.num_and_special_passwords = [""] * self.test_depth
        for num in range(self.test_depth):
            self.num_and_special_passwords[num] = pwgen.gen(self.test_depth, special_chars=True, numbers=True)


    def test_password_length(self):
        for idx, password in enumerate(self.len_passwords):
            self.assertEqual(idx, len(password))

    def test_passwords_with_special_chars_have_special_chars(self):
        import string
        num_specials_each_password = [0] * self.test_depth
        for idx, password in enumerate(self.special_passwords):
            for char in password:
                if char in string.punctuation:
                    num_specials_each_password[idx] += 1
        
        for num in num_specials_each_password:
            self.assertTrue(num > 0)

    def test_passwords_with_numbers_contain_numbers(self):
        import string
        num_digits_each_password = [0] * self.test_depth
        for idx, password in enumerate(self.num_passwords):
            for char in password:
                if char in string.digits:
                    num_digits_each_password[idx] += 1
        
        for num in num_digits_each_password:
            self.assertTrue(num > 0)

    def test_passwords_with_numbers_and_special_chars_havenumbers_and_special_chars(self):
        import string
        num_digits_or_specials_each_password = [0] * self.test_depth
        for idx, password in enumerate(self.num_and_special_passwords):
            for char in password:
                if char in string.punctuation or char in string.digits:
                    num_digits_or_specials_each_password[idx] += 1
        
        for num in num_digits_or_specials_each_password:
            self.assertTrue(num > 0)

    def test_passwords_containing_numbers_have_correct_length(self):
        for password in self.num_passwords:
            self.assertEqual(self.test_depth, len(password))

    def test_passwords_containing_special_chars_have_correct_length(self):
        for password in self.special_passwords:
            self.assertEqual(self.test_depth, len(password))

    def test_passwords_containing_numbers_and_chars_have_correct_length(self):
        for password in self.num_and_special_passwords:
            self.assertEqual(self.test_depth, len(password))

if __name__ == "__main__":
    unittest.main()
