import re

if __name__ == '__main__' :
    n = int(input())
    string = ''
    for _ in range(n):
        user_input = input()
        try:
            re.compile(user_input)
        except:
            print(False)
        else: print(True)

# What I learned:
# 1. What a regex is