import re

if __name__ == '__main__' :
    s = input().strip()
    k = input().strip()
    l = []
    i = 0
    while i <= (len(k)):
        match = re.search(k, s[i:])
        if match:
            l.append(tuple([match.start() + i, match.end() - 1 + i]))
            i += int(match.span()[0]) + 1 
        else: 
            break
    if len(l) == 0:
        l.append((-1, -1))
    for item in l:
        print(item)