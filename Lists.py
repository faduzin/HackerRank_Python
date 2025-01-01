list_commands = {
    "insert": list.insert,
    "remove": list.remove,
    "append": list.append,
    "sort": list.sort,
    "pop": list.pop,
    "reverse": list.reverse,
    "print": lambda list : print(list),
}

if __name__ == '__main__' :
    N = int(input())
    list_output = []
    for _ in range(N):
        input_list = input().split()
        command = input_list[0]
        args = list(map(int, input_list[1:]))
        list_commands[command] (list_output, *args)

# What I learned:
# 1.To read dynamic size inputs you may store them in
# in a list, and pass it as an argument to the
# dictionary
# 2. lambda function in dictionary is an option