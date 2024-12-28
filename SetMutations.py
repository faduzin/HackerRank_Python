update_operations = {
    "update": set.update,
    "intersection_update": set.intersection_update,
    "difference_update": set.difference_update,
    "symmetric_difference_update": set.symmetric_difference_update,
}
sizeA = int(input())
A = set(map(int, input().split()))
for i in range(0,int(input())):
    operation_name = input().split()[0]
    B = set(map(int, input().split()))
    update_operations[operation_name](A, B)
print(sum(A))