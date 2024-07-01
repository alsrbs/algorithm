def make(c, s):
    global num

    if c == n:
        arr[num] = 1
        return

    for i in range(s, 4):
        num += Rome_num[i]
        make(c+1, i)
        num -= Rome_num[i]


n = int(input())
Rome_num = [1, 5, 10, 50]
arr = [0]*1001
num = 0
make(0, 0)
print(sum(arr))