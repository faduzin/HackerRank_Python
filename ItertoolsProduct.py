from itertools import product

if __name__ == '__main__' :
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(*product(A,B))

# What I learned
# 1. The itertools product function
# 2. The way it works, it yields the values
# and by doing that in each iteration it adds
# the values yielded to a list that the
# function returns.
# 3. You can print using *something, which 
# prints the content of something and not
# itself, it does that by passing each
# content as a separate argument
