print(len(list((lambda x: filter(lambda y: all(map(lambda z: z in y, x[1])), x[0]))([open('day4.in','r').read().split('\n\n'), ['byr','iyr','eyr','hgt','hcl','ecl','pid']]))))
