input_list = [7, 4, 9, 2, 5, 1]
A = []

for num in input_list:
    if num % 2 == 0:
        A.append(num)

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

print(A)  
