if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        set_a = set(map(int, input().split()))
        m = int(input())
        set_b = set(map(int, input().split()))
        print(set_a.issubset(set_b))