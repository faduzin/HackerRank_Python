if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print((lambda x, y : x + y)(a,b))
    print((lambda x, y : x - y)(a,b))
    print((lambda x, y : x * y)(a,b))