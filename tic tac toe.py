arr = ['.']*9


def rowCheck(_, ch):
  for __ in range(3):
    if arr[_*3+__] != ch:
      return False
  return True

def row(ch):
  return any(map(rowCheck,([i,ch] for i in range(3))))

won = False
while not won:
  #player input with verification
  (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda f: (lambda a: (__import__("operator").setitem(arr,(a[0]-1)*3+a[1]-1,'x')) if (a[0] in [1,2,3] and a[1] in [1,2,3] and arr[(a[0]-1)*3+a[1]-1] == '.') else f(map(int,raw_input().split()))))(map(int,raw_input().split()))
  print "\n".join(map(lambda z: "".join(arr[z*3:(z+1)*3]), [0,1,2]))


  #random input
  (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda f: (lambda a: (__import__("operator").setitem(arr,(a[0]-1)*3+a[1]-1,'o')) if (a[0] in [1,2,3] and a[1] in [1,2,3] and arr[(a[0]-1)*3+a[1]-1] == '.') else f([__import__("random").randint(1,3),__import__("random").randint(1,3)])))([__import__("random").randint(1,3),__import__("random").randint(1,3)])
  print "\n".join(map(lambda z: "".join(arr[z*3:(z+1)*3]), [0,1,2]))

(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda f: (lambda a: (__import__("operator").setitem(arr,(a[0]-1)*3+a[1]-1,'x')) if (a[0] in [1,2,3] and a[1] in [1,2,3] and arr[(a[0]-1)*3+a[1]-1] == '.') else f(map(int,raw_input().split()))))(map(int,raw_input().split()))
print "\n".join(map(lambda z: "".join(arr[z*3:(z+1)*3]), [0,1,2]))
