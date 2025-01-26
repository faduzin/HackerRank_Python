import re

regex_pattern = r"(?!.*(I{4}|V{2,}|X{4}|L{2,}|D{2,}|M{4}|C{4})).*$"

if __name__ == '__main__' :
    print(str(bool(re.match(regex_pattern, input()))))