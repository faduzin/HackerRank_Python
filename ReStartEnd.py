import re

if __name__ == '__main__' :
    s = input().strip()
    k = input().strip()
    l = []
    for i in range (len(k)+1):
        match = re.search(k, s[i:])
        if match:
            l.append(tuple([match.start() + i, match.end() - 1 + i])) 
    for item in l:
        print(item)
    else: print("(-1, -1)")