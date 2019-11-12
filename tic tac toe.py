arr = ['.']*9
t = [0,1,2]
var = 1
won = False

def diag1(ch):
  for _ in t:
    if arr[_*4] != ch:
      return False
  return True


while not won:
  var = var * -1
  #input with verification
  (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda f: (lambda a: (__import__("operator").setitem(arr,(a[0]-1)*3+a[1]-1,'x' if var == -1 else 'o')) if (a[0]-1 in t and a[1]-1 in t and arr[(a[0]-1)*3+a[1]-1] == '.') else f(map(int,raw_input().split()) if var==-1 else [__import__("random").randint(1,3),__import__("random").randint(1,3)])))(map(int,raw_input().split()) if var==-1 else [__import__("random").randint(1,3),__import__("random").randint(1,3)])

  print (lambda ch: any(map(lambda a: all(map(lambda __: False if arr[a[0]*3+__] != a[1] else True, t)),([i,ch] for i in t))))('x' if var == -1 else 'o')
  print (lambda ch: any(map(lambda a: all(map(lambda __: False if arr[__*3+a[0]] != a[1] else True, t)),([i,ch] for i in t))))('x' if var == -1 else 'o')
  print not any(map(lambda c: c=='.', arr))


  print "\n".join(map(lambda z: "".join(arr[z*3:(z+1)*3]), t))
