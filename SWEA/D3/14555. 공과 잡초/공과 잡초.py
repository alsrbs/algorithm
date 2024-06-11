for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    field=input()
    print(field.count('(')+field.count(')')-field.count('()'))