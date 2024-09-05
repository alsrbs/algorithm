count = {'Cc': 0, 'Pt': 0, 'Re': 0, 'Tb': 0, 'Cm': 0, 'Ea': 0, 'Ex': 0}
total_count = 0

while True:
    try:
        temp = list(map(str, input().split()))

        for i in temp:
            if i in count:
                count[i] += 1
            total_count += 1

        if len(temp) == 0:
            break

    except:
        break


print('Re', count['Re'], "{:.2f}".format(count['Re']/total_count))
print('Pt', count['Pt'], "{:.2f}".format(count['Pt']/total_count))
print('Cc', count['Cc'], "{:.2f}".format(count['Cc']/total_count))
print('Ea', count['Ea'], "{:.2f}".format(count['Ea']/total_count))
print('Tb', count['Tb'], "{:.2f}".format(count['Tb']/total_count))
print('Cm', count['Cm'], "{:.2f}".format(count['Cm']/total_count))
print('Ex', count['Ex'], "{:.2f}".format(count['Ex']/total_count))
print('Total', total_count, "{:.2f}".format(1.00))