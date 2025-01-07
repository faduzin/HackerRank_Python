from collections import namedtuple

if __name__ == '__main__' :
    n = int(input())
    sum = 0
    Student = namedtuple('Student', input())
    for _ in range(n):
        student_x = Student(*input().split())
        sum += int(student_x.MARKS)
    print(sum/n)

# What I learned:
# 1. namedtuple function and how to use it
# 2. When the function takes a variable amount
# of arguments, you must add the operator *