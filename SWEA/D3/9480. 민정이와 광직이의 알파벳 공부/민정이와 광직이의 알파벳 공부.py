def check(string): # 소문자 26개가 다 있으면 True 리턴
    answer = "abcdefghijklmnopqrstuvwxyz"
    string = list(set(string))
    cnt = 0
    for st_ in string:
        if st_ in answer:
            cnt += 1
    if cnt == 26:
        return 1
    return 0

def dfs(idx, depth, string): # 조합을 구현하여 단어를 이어 붙힘
    global answer
    answer += check(string)
    if depth == N:
        return
    for i in range(idx, N):
        dfs(i+1, depth+1, string+alpha[i])

for tc in range(1, int(input())+1):
    N = int(input())
    alpha = [input() for _ in range(N)]
    answer = 0
    dfs(0, 0, "")
    print(f"#{tc}", answer)