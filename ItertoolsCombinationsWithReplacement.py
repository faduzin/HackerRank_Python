from itertools import combinations_with_replacement as combinations

if __name__ == '__main__':
    string, k= map(str, input().split())
    set = set(combinations(sorted(string), int(k)))
    for item in sorted(set):
        print("".join(item))