bracket = input()

while '()' in bracket:
    bracket = bracket.replace('()', '')
print(len(bracket))
