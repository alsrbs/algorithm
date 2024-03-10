record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
user_nickname = {}

message = []

for i in record:
    user = i.split()
    if user[0] == 'Enter':
        user_nickname[user[1]] = user[2]
        message.append([user[1], "님이 들어왔습니다."])
    elif user[0] == 'Leave':
        message.append([user[1], "님이 나갔습니다."])
    elif user[0] == 'Change':
        user_nickname[user[1]] = user[2]

result = []
for i in message:
    result.append(str(user_nickname[i[0]]) + i[1])