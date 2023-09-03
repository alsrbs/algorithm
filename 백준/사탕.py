n = int(input())
lst = [int(input()) for _ in range(n)]

list_s = []

num = lst[0]+lst[-1]
first = 0
# 연립방정식을 사용하여 첫번째 수를 찾는다
for i, v in enumerate(lst):
    if i%2 == 0:
        first += v
    else:
        first -= v
list_s.append(first//2)

# 순회하며 다른 학생들의 사탕 수를 찾는다.
for i in range(n-1):
    list_s += [lst[i] - list_s[i]]

for i in list_s:
    print(i)
