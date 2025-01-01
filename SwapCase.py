def swap_case(s):
    changed_string = ''
    for i in range(len(s)):
        if s[i].islower():
            changed_string += changed_string.join(s[i].upper())
        elif s[i].isupper():
            changed_string += changed_string.join(s[i].lower())
        else:
            changed_string += changed_string.join(s[i])
    return changed_string

if __name__ == '__main__' :
    s = input()
    s = swap_case(s)
    print(s)

# What I learned:
# 1. string.join returns only the value with pass as parameter
# is this value is a character of the string, you must use
# increment to add the join into the string