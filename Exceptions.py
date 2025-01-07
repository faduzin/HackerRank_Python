if __name__ == '__main__' :
    n = int(input())
    for _ in range(n):
        try:
            a , b = map(int, input().split())
        except ValueError as e:
            print("Error Code:", e)
            continue
        try:
            print(int(a/b))
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
            continue

# What I learned:
# 1. How to handle errors
# 2. How to use try and except