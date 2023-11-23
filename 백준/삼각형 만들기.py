import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list += [int(input())]
num_list.sort(reverse=True)

result = -1
for i in range(N-2):
    if num_list[i] < num_list[i+1] + num_list[i+2]:
        result += num_list[i] + num_list[i+1] + num_list[i+2] + 1
        break
print(result)
