def next_permutation(arr):
    k = -1
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            k = i

    if k == -1:
        return

    l = -1
    for i in range(k + 1, len(arr)):
        if arr[k] < arr[i]:
            l = i

    arr[k], arr[l] = arr[l], arr[k]

    arr[k + 1:] = reversed(arr[k + 1:])

    return True


for _ in range(int(input())):
    word = list(input())
    next_permutation(word)
    print(''.join(word))