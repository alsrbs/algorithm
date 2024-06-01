password = list(map(int, input().split()))
print((password[0]**2 + password[1]**2 + password[2]**2 + password[3]**2 + password[4]**2)%10)