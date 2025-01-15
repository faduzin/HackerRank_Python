from collections import deque

operations = {
    "append": deque.append,
    "pop": deque.pop,
    "popleft": deque.popleft,
    "appendleft": deque.appendleft
}

if __name__ == '__main__':
    d = deque()
    n = int(input())
    for _ in range(n):
        input_list = list(input().split())
        command = input_list[0]
        if command == "pop" or command == "popleft":
            operations[command](d)
            continue
        value = int(input_list[1])
        operations[command](d, value)
    for item in d:
        print(item, end=" ")