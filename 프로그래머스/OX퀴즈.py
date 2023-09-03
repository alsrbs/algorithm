def solution(quiz):
    lst = []
    for i in quiz:

        num1 = int(i.split()[0])
        num2 = int(i.split()[2])
        num3 = int(i.split()[4])

        if i.split()[1] == '-':
            if (num1 - num2) == num3:
                lst += ['O']
            else:
                lst += ['X']

        else:
            if (num1 + num2) == num3:
                lst += ['O']
            else:
                lst += ['X']

    return lst