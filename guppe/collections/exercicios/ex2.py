
A: list[int] = [1, 0, 5, -2, -5, 7]


soma = sum(A[0:2]) + A[5]
print('------')
print(soma)
print('------')

# A.insert(5, 100)
A[5] = 100
for elem in A:
    print(elem)
