if __name__ == '__main__' :
    s = input()
    s = s.strip()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for i in range(len(s)):
        if not alnum:
            alnum = s[i].isalnum()
        if not alpha:
            alpha = s[i].isalpha()
        if not digit:
            digit = s[i].isdigit()
        if not lower:
            lower = s[i].islower()
        if not upper:
            upper = s[i].isupper()
        if alnum * alpha * digit * lower * upper:
            break
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

    # What I learned:
    # 1. Some of the build in string verification functions.
    # 2. When only one argument is passed to range, it goes
    # from 0 to that number.
    # 3. To negate a value you put 'not'