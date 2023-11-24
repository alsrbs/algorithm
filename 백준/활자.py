N = int(input())
num = 9
if N < 10:
    print(N)
else:
    for i in range(2, len(str(N))+1):
        if len(str(N)) == i:
            num += (N-(int('9' * (len(str(N))-1)))) * (len(str(N)))
        else:
            num += (int('9'*i) - int('9'*(i-1))) * i
    print(num % 1234567)
