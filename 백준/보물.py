N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)
num = 0
for i in range(N):
    num += A[i] * B[i]
print(num)
# A 오름차순 정렬
# B 내림차순 정렬
# 큰 수 와 작은 수를 곱하게하여 최솟값을 출력