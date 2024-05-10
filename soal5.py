input_list = [105, 20, 8, 150, 30, 5, 200]
A = []

for num in input_list:
    if 10 <= num <= 100:
        A.append(num)

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

print(A)
