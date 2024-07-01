n = int(input())
s, e = input().split('*')
l = len(s) + len(e)

for i in range(n):
    word = input()
    if l > len(word):
        print('NE')
    else:
        if word[:len(s)] == s and word[-len(e):] == e:
            print('DA')
        else:
            print('NE')