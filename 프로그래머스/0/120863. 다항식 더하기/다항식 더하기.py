def solution(polynomial):
    x = 0
    num = 0
    polynomial = polynomial.split()
    for i in range(0, len(polynomial), 2):
        if 'x' in polynomial[i]:
            if 'x' == polynomial[i]:
                x += 1
            else:
                x += int(polynomial[i][:-1])
        else:
            num += int(polynomial[i])       
            
    if num and x:
        if x == 1:
            return f'x + {num}' 
        return f'{x}x + {num}' 
    if num and x == 0:
        return str(num)
    if x == 1:
        return 'x'
    return f'{x}x'