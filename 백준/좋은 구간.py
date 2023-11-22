
L = int(input())
list_S = sorted(map(int, input().split()))
n = int(input())
if n in list_S:
    print(0)
else:
    A, B = 0, 0
    arr = []
    if n < list_S[0]:
        for i in range(1, list_S[0]):
            arr += [i]
        print((n-1)*(list_S[0]-n) + list_S[0]-n-1)

    else:
        for i in range(L-1):
            if list_S[i] < n < list_S[i+1]:
                A = list_S[i]+1
                B = list_S[i+1]
                break
        print((n-A)*(B-n)+(B-n-1))

