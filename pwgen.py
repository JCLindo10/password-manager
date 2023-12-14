"""

pwgen.py

Created: 11/17/2023
Author: Jakob Lindo

Code for basic password generation

"""

import string
import random
alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
specials = list(string.punctuation)
digits = list(string.digits)
charset = []

def pw_has_required_complexity(pw: str, special_chars: bool, numbers: bool) -> bool:
    if special_chars and digits:
        return any(char in specials + numbers for char in pw)
    if special_chars and not digits:
        return any(char in specials for char in pw)
    if not special_chars and digits:
        return any(char in digits for char in pw)
    return True # pw only has letters

def gen(length: int, special_chars: bool = False, numbers: bool = False) -> str:
    '''
    Returns a randomly generated password

        Parameters:
            length (int): Desired length of the password
            special_chars (bool): Choice of including special characters
            numbers (bool): Choice of including numbers

        Returns:
            password (str): password 

    '''

    if length < 7:
        return ''

    password = ''


    if special_chars and numbers:
        charset = alphabet + specials + digits
        random.shuffle(charset)

        password = ( # ensures that password contains at least one of each type of char
        random.choice(alphabet) +
        random.choice(digits) +
        random.choice(specials)
        )
        password = password + ''.join(random.choice(charset) for _ in range(length - 3))
    elif special_chars and not numbers:
        charset = alphabet + specials
        random.shuffle(charset)

        password = ( # ensures that password contains at least one of each type of char
        random.choice(alphabet) +
        random.choice(specials)
        )
        password = password + ''.join(random.choice(charset) for _ in range(length - 2))
    elif not special_chars and numbers:
        charset = alphabet + digits
        random.shuffle(charset)

        password = ( # ensures that password contains at least one of each type of char
        random.choice(alphabet) +
        random.choice(digits) 
        )
        password = password + ''.join(random.choice(charset) for _ in range(length - 2))
    else:
        charset = alphabet
        random.shuffle(charset)
        password = random.choice(alphabet)
        password = password + ''.join(random.choice(charset) for _ in range(length - 1))


    return password

if __name__ == "__main__":
    print(gen(0))
