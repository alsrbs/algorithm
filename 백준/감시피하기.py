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

# 문자열로 변환하여 중복을 제거합니다.
unique_list = [tuple(map(str, sublist)) for sublist in W]
unique_list = list(set(unique_list))
# 다시 원래 형식으로 변환
unique_list = [list(map(eval, sublist)) for sublist in unique_list]

if len(unique_list) > 3:
    vs = 'NO'
print(vs)

# 윤동훈 ============================================================================
import copy
from itertools import combinations

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def is_possible(can_pos_list,arr):
    temp_arr = copy.deepcopy(arr)
    for i in can_pos_list:
        temp_arr[i[0]][i[1]] = "O"

    for i in T_pos:
        r,c = i
        for idx in range(4):
            temp_r,temp_c = r,c
            while True:
                nr = temp_r + dr[idx]
                nc = temp_c + dc[idx]
                if 0 <= nr < N and 0 <= nc < N and (temp_arr[nr][nc] == "X" or temp_arr[nr][nc] == "S" or temp_arr[nr][nc] == "T"):
                    temp_arr[nr][nc] = "T"
                    temp_r, temp_c = nr, nc
                else: break

    S_cnt = 0
    for i in range(len(temp_arr)):
        for j in range(len(temp_arr)):
            if temp_arr[i][j] == "S":
                S_cnt += 1

    if S_cnt == len(S_pos): return True
    else: return False


# ==================================================================

N = int(input())
arr = [list(input().split()) for _ in range(N)]

can_insert = []
T_pos = []
S_pos = []

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 'X': can_insert.append((i,j))
        elif arr[i][j] == 'T': T_pos.append((i,j))
        else: S_pos.append((i,j))


for i in combinations(can_insert,3):
    answer = is_possible(list(i),arr)
    if answer:
        print("YES")
        break
    else: continue
else:
    print("NO")
