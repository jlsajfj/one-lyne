arr = ['.']*9


won = False
var = -1
while not won:
  #input with verification
  (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda f: (lambda a: (__import__("operator").setitem(arr,(a[0]-1)*3+a[1]-1,'x' if var == -1 else 'o')) if (a[0] in [1,2,3] and a[1] in [1,2,3] and arr[(a[0]-1)*3+a[1]-1] == '.') else f(map(int,raw_input().split()) if var==-1 else [__import__("random").randint(1,3),__import__("random").randint(1,3)])))(map(int,raw_input().split()) if var==-1 else [__import__("random").randint(1,3),__import__("random").randint(1,3)])

  print (lambda ch: any(map(lambda a: all(map(lambda __: False if arr[a[0]*3+__] != a[1] else True, [0,1,2])),([i,ch] for i in range(3)))))('x')
  print not any(map(lambda c: c=='.', arr))

  var = var * -1

  print "\n".join(map(lambda z: "".join(arr[z*3:(z+1)*3]), [0,1,2]))
