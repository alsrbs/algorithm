n, m = map(int, input().split())

min_package = 9999
min_each = 9999
for _ in range(m):
    package, each = map(int, input().split())
    min_package = min(min_package, package)
    min_each = min(min_each, each)

if min_package > min_each*6:
    print(n*min_each)
else:
    if min_package < (n%6)*min_each:
        print(((n//6)*min_package) + min_package)
    else:
        print(((n//6)*min_package) + ((n%6)*min_each))
