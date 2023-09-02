dr = [-1,0,0,1]
dc = [0,1,-1,0]

N = int(input())
arr = [list(input().split()) for i in range(N)]
W = []

# 선생과 학생의 마주친 경로
def check(r,c):
    global W
    for i in range(4):
        lst = []
        nr = r
        nc = c
        while True:
            nr += dr[i]
            nc += dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                lst.append((nr, nc))
                if arr[nr][nc] == 'S':
                    W += [lst[:-1]]
                    break
            else:
                break

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            check(i,j)

vs = 'YES'
lst = []
for i in range(len(W)):
    if not W[i]:
        vs='NO'
        break
    # 결로가 중복된 구간이 있을 경우 해당 경로를 변경
    for j in W[i]:
        for k in range(len(W)):
            if i != k and j in W[k]:
                W[i] = W[k]
                break

# 각 서브리스트를 정렬하고 문자열로 변환하여 중복을 제거합니다.
unique_list = [tuple(map(str, sublist)) for sublist in W]
unique_list = list(set(unique_list))
# 다시 원래 형식으로 변환합니다.
unique_list = [list(map(eval, sublist)) for sublist in unique_list]

if len(unique_list) > 3:
    vs = 'NO'
print(vs)
