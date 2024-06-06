for t in range(1, int(input())+1):
    print(f'#{t}')
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    clock_90 = list(map(list, zip(*arr[::-1])))
    clock_180 = list(map(list, zip(*clock_90[::-1])))
    clock_270 = list(map(list, zip(*clock_180[::-1])))

    for i in range(n):
        print("".join(map(str,clock_90[i])), end=" ")
        print("".join(map(str,clock_180[i])), end=" ")
        print("".join(map(str,clock_270[i])), end="\n")