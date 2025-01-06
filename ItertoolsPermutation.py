from itertools import permutations

def permute(string, k):
    permutations_list = list(permutations(string, k))
    permutations_list.sort()
    for i in range(len(permutations_list)):
        permutation = ''
        for j in range(k):
            permutation += permutations_list[i][j]
        print(permutation)

if __name__ == '__main__':
    string, k = input().split()
    k = int(k)
    permute(string, k)

# What I learned;
# 1. A new function permutations
# 2. Got the solution
# 3. The most optimized way:
# from itertools import permutations 
# s,k = input().split() 
# res = sorted(permutations(s,int(k))) 
# for i in res: 
#     print("".join(i))