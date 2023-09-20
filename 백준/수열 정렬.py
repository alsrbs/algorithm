A_size = int(input())
A = list(map(int, input().split()))
sorted_A = sorted(A)

P = []
for i in A:
    P += [sorted_A.index(i)]
    sorted_A[sorted_A.index(i)] = -1
print(*P)