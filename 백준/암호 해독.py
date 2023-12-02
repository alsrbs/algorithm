key = input()
password = input()
dic_password = {}
sort_key = sorted(key)
for i in range(len(key)):
    dic_password[i] = sort_key[i] + password[(len(password)//len(key))*i:(i+1)*(len(password)//len(key))]

print(dic_password)
# result = ''
# for i in range(len(dic_password[key[0]])):
#     for k in range(len(key)):
#         result += dic_password[key[k]][i]
#
# print(result)