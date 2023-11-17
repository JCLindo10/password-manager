import pwgen

if __name__ == "__main__":
    print(pwgen.gen(10), pwgen.gen(10, True, True), pwgen.gen(10, True, False), pwgen.gen(10, False, True))