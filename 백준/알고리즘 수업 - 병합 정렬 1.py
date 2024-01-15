def merge_sort(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    i = p
    j = q+1
    t = 0
    tmp = [0] * (r - p + 1)
    while i <= q and j <= r:
        if A[i] <= A[j]:
            temp.append(A[i])
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            temp.append(A[j])
            tmp[t] = A[j]
            t += 1
            j += 1
    while i <= q:
        temp.append(A[i])
        tmp[t] = A[i]
        t+=1
        i+=1
    while j <= r:
        temp.append(A[j])
        tmp[t] = A[j]
        t+=1
        j+=1
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        t+=1
        i+=1

l, idx = map(int, input().split())
arr = list(map(int, input().split()))
temp = []
merge_sort(arr, 0, len(arr) - 1)
if idx >= len(temp):print(-1)
else:print(temp[idx-1])
