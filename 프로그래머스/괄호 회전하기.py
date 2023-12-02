from collections import deque

def Rotate(s):
    stack = []
    if s[0] == ']' or s[0] == '}' or s[0] == ')':
        return 0
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)
    return 1 if len(stack) == 0 else 0

s = "[](){}"
s = deque(s)
answer = 0
if s.count('[') - s.count(']') + s.count('{') - s.count('}') + s.count('(') - s.count(')') != 0:
    print(answer)
else:
    for i in range(len(s)):
        s.rotate(-1)
        answer += Rotate(s)
print(answer)
