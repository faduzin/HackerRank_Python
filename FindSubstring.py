def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)-len(sub_string)+1):
        equal_char_count = 0
        for j in range(0, len(sub_string)):
            if string[i+j] == sub_string[j]:
                equal_char_count += 1
            if equal_char_count == len(sub_string):
                count += 1
            if equal_char_count < j+1:
                break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# What I learned:
# 1. A string may be accessed like a list of chars
# 2. The way made was not optimized as I compared
# character by character whe I could actually use
# slicing like in:
# def count_substring(string, sub_string):
    # count = 0
    # for i in range(len(string) - len(sub_string) + 1):
    #     if string[i:i+len(sub_string)] == sub_string:
    #         count += 1
    # return count
# This would compare the whole string at once.