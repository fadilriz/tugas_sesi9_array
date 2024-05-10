arr_1 = [8, 3, 12, 4, 7, 2]

for i in range(len(arr_1)):
    if arr_1[i] < 5:
        arr_1[i] = 0

arr_1.sort(reverse=True)

print(arr_1)
