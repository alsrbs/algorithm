import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
n_list = ''.join(list(input().strip()))
m_list = ''.join(list(input().strip()))

if n > m:
    print('normal')
else:
    if m_list.count(n_list):
        print('secret')
    else:
        print('normal')

