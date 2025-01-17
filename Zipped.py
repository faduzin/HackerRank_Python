if __name__ == '__main__' :
    x, n = map(int, input().split())
    grades = [tuple(map(float, input().split())) for _ in range(n)]
    zipped_grades = zip(*grades)
    [print(sum(student)/len(student)) for student in zipped_grades]