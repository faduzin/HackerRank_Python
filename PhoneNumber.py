import re
regex_pattern = r"^[789]{1}\d{9}"

if __name__ == '__main__' :
    for _ in range(int(input())):
        string = input()
        print("YES" if (bool(re.match(regex_pattern, string))and (len(string) == 10)) else "NO")