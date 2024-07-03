gwalho = input()
stack = []
ans = 0
for i in range(len(gwalho)):
    if gwalho[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if gwalho[i-1] == '(':
            ans += len(stack)
        else:
            ans += 1

print(ans)