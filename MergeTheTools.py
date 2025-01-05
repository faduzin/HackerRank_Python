def merge_the_tools(string, k):
    count = 0
    repetition = 0
    list = []
    list.append('')
    if not len(string) or k == 0:
        return
    for i in range(len(string)):
        count +=1
        list[repetition] += string[i]
        if count == k:
            count = 0
            set_char = set(list[repetition])
            u = ''
            for char in set_char:
                u += char
            print(u)
            repetition += 1
            list.append('')


if __name__ == '__main__' :
    string, k = input(), int(input())
    merge_the_tools(string, k)

# What I learned:
# 1. I am capable of solving medium difficulty problems!