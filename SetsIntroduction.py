def average(array):
    array = set(array)
    return sum(array)/len(array)

if __name__ =='__main__' :
    N = int(input())
    array = list(map(int, input().split()))
    print(average(array))