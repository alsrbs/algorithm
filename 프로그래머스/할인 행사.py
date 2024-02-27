want = list(input().split())
number = list(map(int, input().split()))
discount = list(input().split(','))

want_list = []
for i in range(len(want)):
    want_list += [want[i]]*number[i]

want_list.sort()
cnt = 0
for i in range(len(discount) - 9):
    if want_list == sorted(discount[i:i+10]):
        cnt += 1

print(cnt)
