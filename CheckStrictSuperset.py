if __name__ == '__main__':
    set_a = set(map(int, input().split()))
    status = True
    for _ in range(int(input())):
        if not set_a.issuperset(set(map(int, input().split()))):
            status = False
            break
    print(status)