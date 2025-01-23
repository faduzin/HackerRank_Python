import re
regex_pattern = r'([a-zA-Z0-9])\1+'

if __name__ == '__main__':
    l = re.findall(regex_pattern, input())
    print(l[0] if len(l) != 0 else -1)