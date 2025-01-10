if __name__ == '__main__' :
    m = int(input())
    set1 = set(map(int, input().split()))
    n = int(input())
    set2 = set(map(int, input().split()))
    for item in sorted(set1.symmetric_difference(set2)):
        print(item)

# What I learned:
# 1. How to print sets
# 2. sorted()