import math
import os
import random
import re
import sys

def solve(s):
    splitted_string = s.split(' ')
    result = ''

    for word in splitted_string :
        separated_word = ''
        separated_word = list(word.strip())
        if separated_word:
            separated_word[0] = separated_word[0].upper()
        joined_word = ''
        
        for char in separated_word:
            joined_word += char
        
        result += joined_word + " "
    
    return result

if __name__ == '__main__' :
    s = input()
    result = solve(s)
    print(result)

    # Not sure why the code in the website looked like this:
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = input()
    # result = solve(s) 
    # fptr.write(result + '\n')
    # fptr.close()

# What I learned:
# 1. To join words you can simply sum them, no need to use join
# 2. The return of split() is iterable
# 3. My solution was too big, as I did not use capitalize()
# 4. The smaller solution would be:
# def solve(s):
#     list = ''
#     for word in s.split(' '):
#         list += word.capitalize() + ' '
#     return list