from collections import defaultdict

if __name__ == '__main__' :
    n, m = map(int, input().split())
    dict = defaultdict(list)
    for _ in range(n):
        dict['a'].append(input())
    for _ in range(m):
        value = input()
        found = -1
        for i in range(len(dict['a'])):
            if dict['a'][i] == value:
                print(i+1, sep='', end=' ')
                found = 0
        if found == -1:
            print(found, end='')
        print()

# What I learned:
# 1. One use of dict, and the difference
# between a normal dict and a default one
# 2. Once again, my solution was not the
# best, that would be:
# defaultdict n,m = list(map(int, input().split()))
# A = defaultdict(list) 
# for i in range(1, n+1): 
#     A[input()].append(i)
# for _ in range(m): 
#     print(*A[input()] or [-1])