def average(array):
    array = set(array)
    return sum(array)/len(array)

if __name__ =='__main__' :
    N = int(input())
    array = list(map(int, input().split()))
    print(average(array))

# What I learned:
# 1. You can use len when data is a set
# 2. A set returns the ordered unique values of a list