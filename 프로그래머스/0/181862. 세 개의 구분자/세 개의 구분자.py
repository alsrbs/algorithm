def solution(myStr):
    answer = []
    st = ''
    for i in myStr:
        if i in ['a', 'b', 'c']:
            if st:
                answer.append(st)
            st = ''
        else:
            st += i
            
    if st:
        answer.append(st)
        
    if answer:
        return answer
    return ["EMPTY"]