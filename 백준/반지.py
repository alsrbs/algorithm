word = input()
N = int(input())
num = 0
for i in range(N):
    st = input()
    st += st
    if word in st:
        num += 1
print(num)