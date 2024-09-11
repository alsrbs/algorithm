n = int(input())
DNA = list(input())
DNA_dic = {'AA': 'A', 'AG': 'C', 'AC': 'A', 'AT': 'G', 'GA': 'C', 'GG': 'G', 'GC': 'T', 'GT': 'A',
       'CA': 'A', 'CG': 'T', 'CC': 'C', 'CT': 'G', 'TA':'G', 'TG': 'A', 'TC': 'G', 'TT': 'T'}

while len(DNA) > 1:
    x = DNA_dic[DNA[-2]+DNA[-1]]
    del DNA[-2:]
    DNA.append(x)

print(DNA[0])