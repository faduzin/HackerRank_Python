k = int(input())
room_list = list(map(int, input().split()))
unique = list(set(room_list))
for i in unique:
    count = 0
    for j in range(0, len(room_list)):
        if i == room_list[j]:
            count += 1
        if count > 1:
            break
        if j == len(room_list)-1 and count == 1:
            print(i)