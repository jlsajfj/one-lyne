print(len(list(filter(lambda ps: (lambda x: (lambda m: m[0] <= x and x <= m[1])(list(map(int,ps[0][0].split('-')))))(ps[1].count(ps[0][1])), map((lambda x: [x[0].split(' '),x[1].strip()]),map(lambda x: x.split(':'),open('day2.in','r').read().strip().split('\n')))))))
