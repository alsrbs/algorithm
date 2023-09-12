a, b, g = map(int, input().split())
A = input().split()
B = input().split()
G = input().split()
total_a = 0
total_b = 0
for i in range(g):
    if G[i] in A:
        total_a += 1
    else:
        total_b += 1
if total_a>total_b:
    print('A')
elif total_a < total_b:
    print('B')
else:
    print("TIE")