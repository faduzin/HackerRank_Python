def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__' :
    line = input()
    result = split_and_join(line)
    print(result)

# What I learned:
# 1. The split function takes the
# separator as argument
# 2. The join function when called
# by a string, uses that string as
# the separator and joins a list
# passed as argument