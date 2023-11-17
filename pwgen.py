"""

pwgen.py

Created: 11/17/2023
Author: Jakob Lindo

Code for basic password generation

"""

import string
import random


def gen(length: int, special_chars: bool, numbers: bool) -> str:
    '''
    Returns a randomly generated password

        Parameters:
            length (int): Desired length of the password
            special_chars (bool): Choice of including special characters
            numbers (bool): Choice of including numbers

        Returns:
            password (str): password 

    '''
    password = [""] * length
    alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
    specials = list(string.punctuation)
    numbers = list(string.digits)

    
    

    return str(password)

