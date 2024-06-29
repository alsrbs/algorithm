def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


n = int(input())
n_nums = list(map(int, input().split()))
m = int(input())
m_nums = list(map(int, input().split()))

n_num = 1
for i in range(n):
    n_num *= n_nums[i]

m_num = 1
for i in range(m):
    m_num *= m_nums[i]

x = gcd(n_num, m_num)
print(str(x)[-9:])