if __name__ == '__main__':
    x, k = map(int, input().split())
    polinomial = input()
    polinomial.replace("x", str(x))
    print(eval(polinomial) == k)