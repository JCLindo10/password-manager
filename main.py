"""

main.py

Created: 11/29/23
Author: Jakob Lindo

Main driver program

"""

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--num_chars", action="store", type="int", dest="password_length")
parser.add_option("-s", "--special_chars", action="store_true", dest="special_chars")
parser.add_option("-d", "--numerics", action="store_true", dest="numerical_chars")

def main():
    pass


if __name__ == "__main__":
    main()