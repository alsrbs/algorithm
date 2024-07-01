import sys
input = sys.stdin.readline

k, l = map(int, input().split())
arr_idx = dict()

for i in range(l):
    Student_ID = input().strip()
    arr_idx[Student_ID] = i

arr = sorted(arr_idx.items(), key=lambda x:x[1])

for i in range(min(k, len(arr))):
    print(arr[i][0].strip())