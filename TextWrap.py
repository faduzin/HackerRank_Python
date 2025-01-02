import textwrap

# def wrap(string, max_width):
#     new_string = ''
#     string = string.strip()
#     for i in range(0, len(string) -1, max_width):
#         for j in range(max_width):
#             if i+j >= len(string):
#                 break
#             new_string += new_string.join(string[i+j])
#         if i+max_width < len(string):
#             new_string += new_string.join("\n")
#     return new_string

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# What I learned;
# 1. textwrap would make it simple to solve the problem
# as my first implementation without using it was big
# 2. textwrap will only break long words if there are not
# hyphens or spaces between words, unless you set the
# parameter break_long_words to False