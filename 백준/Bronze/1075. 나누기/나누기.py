n = int(input())
f = int(input())

num = n - n%100

answer = None
for i in range(100):
    if num%f == 0:
        answer = str(num)
        break
    num += 1

print(answer[-2:])