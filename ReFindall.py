import re
vowels = "aeiouAEIOU"
consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
pattern = r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])'

if __name__ == '__main__':
    matches = re.findall(pattern, input())
    if matches:
        for match in matches:
            print(match)
    else:
        print(-1)