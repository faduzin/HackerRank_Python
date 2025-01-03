def print_rangoli(size):
    width = 4*(size -1) + 1
    for i in range(1 , size + 1):
        string = ''
        for j in range(i, 1, -1):
            string += string.join(chr(ord('`')+size-i+j))
            string += string.join('-')
        for j in range(1, i+1):
            string += string.join(chr(ord('`')+size-i+j))
            if j == i:
                continue
            string += string.join('-')
        print(string.center(width, '-'))
    
    for i in range(size-1, 0, -1):
        string = ''
        for j in range(i, 1, -1):
            string += string.join(chr(ord('`')+size-i+j))
            string += string.join('-')
        for j in range(1, i+1):
            string += string.join(chr(ord('`')+size-i+j))
            if j == i:
                continue
            string += string.join('-')
        print(string.center(width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# What I learned:
# 1. chr function returns the character that represents
# that specified unicode
# 2. ord function returns the integer that represents
# that character
# 3. the lowercase alphabet starts after '`' character 
# in unicode, which is the unicode 96
# 4. It was challenging to understand and implement the
# number logic of numbers and loops