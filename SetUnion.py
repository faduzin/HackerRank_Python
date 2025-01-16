if __name__ == '__main__':
    n = int(input())
    set_a = set(map(int, input().split()))
    m = int(input())
    set_b = set(map(int, input().split()))
    print(len(set_a.union(set_b)))