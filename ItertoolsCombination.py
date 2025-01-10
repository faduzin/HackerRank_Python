from itertools import combinations

if __name__ == '__main__':
    string, k = input().split()
    k = int(k)
    for i in range(1, k+1):
        for item in combinations(sorted(string), i):
            print("".join(item))

# What I learned:
# 1. Practiced the use of join()
# 2. combinations()
# 3. Practiced the use of sorted to sort a string