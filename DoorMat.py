if __name__ == '__main__' :
    N, M = map(int, input().split())
    base_string = '.|.'

    for i in range(N//2):
        print((base_string*((2*i)+1)).center(M ,'-'))

    print('WELCOME'.center(M, '-'))

    for i in range(N//2 -1, -1, -1):
        print((base_string*((2*i)+1)).center(M ,'-'))

# What I learned:
# 1. It was good practice of already learnt content