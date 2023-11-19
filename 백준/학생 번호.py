def find():
    cnt=1
    while(1):
        if len({i[-cnt:] for i in N_list}) == N:
            return cnt
        cnt = cnt + 1


N = int(input())
N_list = []
for i in range(N):
    N_list.append(input())
res = find()
print(res)