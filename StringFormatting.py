def print_formatted(number):
    pad = len(bin(number)) - 2
    for i in range(1, number+1):
        print(f'{i:{pad}d} {i:{pad}o} {i:{pad}X} {i:{pad}b}')

if __name__ == '__main__' :
    n = int(input())
    print_formatted(n)

# What I learned:
# 1. f string is powerful and can easily do space padding
# 2. The number in the formating of the variable defines
# how many spaces in the padding
# 3. You can use a variable to define de padding size
# 4. It can easily convert the type of a variable just
# by inputting the format, and the available formats
# are: 's':string, 'b':binary, 'c':character, 'd':decimal
# 'o':octal, 'x':hex(lowercase), 'X':hex(uppercase)
# 'n':number (same as 'd' but uses locale setting to insert
# separator characters) and the default is 'd'