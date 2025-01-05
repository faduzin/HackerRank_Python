from collections import Counter

if __name__ == '__main__' :
    x = int(input())
    shoe_size = Counter(map(int, input().split()))  
    n = int(input())
    sum = 0
    for _ in range(n):
        size, offer = map(int, input().split())
        if shoe_size[size] > 0:
            shoe_size[size] -= 1
            sum += offer
    print(sum)

# What I learned:
# 1. How to access and change dictionary values
# 2. The dictionary is now ordered
# 3. The existence of Counter