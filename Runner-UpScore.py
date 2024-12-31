if __name__ == '__main__' :
    n = int(input())
    arr = list(map(int,input().split()))
    setarr = sorted(set(arr), reverse = True)
    print(setarr[1])