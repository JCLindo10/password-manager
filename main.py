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
                    default=0,
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

    password = pwgen.gen(options.password_length, special_chars=options.special_chars, numbers=options.numerical_chars)
        
    print(password)

if __name__ == "__main__":
    main()