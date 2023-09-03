# 고정점 1개만 존재
# 원소가 오름차순 정렬
n = int(input())
lst = list(map(int, input().split()))

def fixed_point(s,e,lst):
    if s>e:
        return -1

    mid = (s+e)//2

    if lst[mid] == mid: # 고정점 발견한 경우 반환
        return mid
    elif lst[mid] > mid:    # 중간점이 작은 경우 왼쪽
        return fixed_point(s,mid-1,lst)
    else:                   # 중간점이 큰 경우 오른쪽
        return fixed_point(mid+1,e,lst)

print(fixed_point(0,n-1,lst))