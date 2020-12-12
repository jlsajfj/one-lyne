print(len(list(filter(lambda x: x[1][3*x[0]%len(x[1])]=='#',enumerate(open('day3.in','r').read().strip().split('\n'))))))
