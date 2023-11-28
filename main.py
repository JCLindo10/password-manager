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
                    help="Boolean denoting the usage of special characters")
parser.add_option("-d", "--numerics",
                    action="store_true",
                    dest="numerical_chars",
                    help="Boolean denoting the usage of numbers")

def main():
    options, args = parser.parse_args()

    print(options, args)




if __name__ == "__main__":
    main()