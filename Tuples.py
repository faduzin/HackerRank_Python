if __name__ == '__main__' :
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))

# What I learned:
# 1. Tuple is one of the four built-in
# data types in python, with List, Set
# and Dictionary
# 2. Tuples don't change after being
# created, so you won't be able to
# add nor remove values
# 3. The value of hash may differ on
# different versions of Python