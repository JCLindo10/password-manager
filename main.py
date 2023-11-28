"""

main.py

Created: 11/29/23
Author: Jakob Lindo

Main driver program

"""

from optparse import OptionParser
import pwgen

parser = OptionParser()
parser.add_option("-n", "--num_chars", 
                    action="store", 
                    type="int", 
                    dest="password_length",
                    help="The length of the desired password")
parser.add_option("-s", "--special_chars",
                    action="store_true", 
                    dest="special_chars",
                    default=False,
                    help="Boolean denoting the usage of special characters")
parser.add_option("-d", "--numerics",
                    action="store_true",
                    dest="numerical_chars",
                    default=False,
                    help="Boolean denoting the usage of numbers")

def main():
    options, args = parser.parse_args()

    print(options, args)
    options_dict = vars(options)
    print(options_dict)

    password = ''
    specials = options.special_chars
    numbers = options.numerical_chars
    length = 0

    if len(options_dict.keys()) == 0:
        password = pwgen.gen()
    
    if 'password_length' in options_dict.keys():
        length = options_dict['password_length']
        
    print(password, specials, numbers)


if __name__ == "__main__":
    main()