import re

if __name__ == '__main__':
    pattern = r'^[+-]?\d*\.\d+$' #^starts with, [] set of char, ? zero or more occurences, \d set of digits, \ escape . special character, + one or more occurences, ends with
    [print(bool(re.match(pattern, input()))) for _ in range(int(input()))]

# This solution almost worked, but there is a test case that requires regex I guess
# if __name__ == '__main__' :
#     list = []
#     [list.append(input()) for _ in range(int(input()))]

#     for item in list:
#         try:
#             float(item)
#         except:
#             print(False)
#             continue
#         print(True)