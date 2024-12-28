if __name__ == '__main__' :
    n = int(input())
    i = 0
    while i < n :
        print((lambda x : x*x)(i))
        i += 1