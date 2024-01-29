N = int(input())
result = ''

while N:

    if N % (-2):
        result = '1' + result
        N = N//-2 + 1

    else:
        result = '0' + result
        N = N//-2

if result:
    print(result)
else:
    print('0')