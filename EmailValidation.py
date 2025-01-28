import email.utils
import re

regex_pattern = r'^[a-z](\w|-|\.)*@[a-z]+\.[a-z]{1,3}$'

if __name__ == '__main__':
    for _ in range(int(input())):
        name, mail = email.utils.parseaddr(input())
        if re.match(regex_pattern, mail):
            print(email.utils.formataddr((name, mail)))