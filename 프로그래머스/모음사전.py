def dfs(i, word):
    global cnt
    cnt += 1
    if word == "IUU":
        print(cnt)
        return
    if i == 5:
        return

    for j in range(5):
        dfs(i+1, word + alphabet[j])


alphabet = ['A', 'E', 'I', 'O', 'U']
cnt = -1
dfs(0, '')