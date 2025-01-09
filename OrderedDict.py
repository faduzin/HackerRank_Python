from collections import OrderedDict

if __name__ == '__main__' :
    n = int(input())
    ordereddict = OrderedDict()
    for i in range(n):
        user_input = input()
        user_input = user_input.rsplit(" ", 1)
        key = user_input[0]
        value = int(user_input[1])
        if key in ordereddict:
            ordereddict[key] += value
        else: 
            ordereddict[key] = value

    for key, value in ordereddict.items():
        print(key, value)

# What I learned:
# 1. OrderedDict and how it works
# 2. How to rsplit()