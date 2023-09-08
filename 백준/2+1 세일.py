from sys import stdin

n = int(input())
list_n = [];total = 0
for i in range(n):
    list_n += [int(stdin.readline())]
list_n.sort(reverse=True)
for i in range(2,n,3):
    total += list_n[i]
print(sum(list_n)- total)
