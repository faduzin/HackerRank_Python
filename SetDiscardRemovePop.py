operations = {
    "remove": set.remove,
    "pop": set.pop,
    "discard": set.discard,
}

if __name__ == '__main__' :
    n = int(input())
    s = set(map(int, input().split()))
    k = int(input())
    for _ in range(k):
        input_list = input().split()
        command = input_list[0]
        if command == "pop":
            operations[command](s)
        else:
            value = int(input_list[1])
            operations[command](s, value)
    print(sum(s))

# What I learned:
# 1. Reinforced my dictionary usage
# 2. The clearer way to solve it would be to:
# N = int(input()) 
# S=set(map(int, input().split()))
# C=int(input())
# ls=[] for _ in range(C): 
#     ls=list(input().split())

# if ls[0]=='pop': 
#     try: 
#         S.pop() 
#     except KeyError: 
#         pass 

# elif ls[0]=='discard':
#     S.discard(int(ls[1])) 

# elif ls[0]=='remove': 
#     try: 
#         S.remove(int(ls[1])) 
#     except KeyError: 
#         pass
# print(sum(S))