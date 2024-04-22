import sys

n=1 #default value

if (len(sys.argv) > 1):
  n=int(sys.argv[1])
else:
  print("No argument provided, default is n=1")

def print_res(l:list):
  for row in l:
    for x in row:
      print(x,end=' ')
    print(' ')

l=list(range(2**n))
for i in range(2**n):
  l[i]=list(range(0,2**n))

def construct(n:int,starti:int,starj:int):
  if(n==1):
    l[starti][startj]='G'
    l[starti][startj+1]='X'
    l[starti+1][startj]='G'
    l[starti+1][startj+1]='G'
    return
  if(n==2):
    flag=False
    if l[starti][startj]!='X' and
l[starti][startj]!='G':
      l[starti][startj]='B'
      l[starti+1][startj+1]='G'
    else :
      flag=True
      l[starti+1][startj+1]='B'
    l[starti][startj+1]='B'
    l[starti][startj+2]='R'
    if l[starti][startj+3]!='X' and 
l[starti][startj+3]!='G':
      l[starti][startj+3]='R'
      l[starti+1][startj+2]='G'
    else:
      flag=True
      l[starti+1][startj+2]='R'
    l[starti+1][startj]='B'
    l[starti+1][startj+3]='R'
    l[starti+2][startj]='R'
    l[starti+2][startj+3]='B'
    if l[starti+3][startj]!='X' and 
l[starti+3][startj]!='G':
      l[starti+3][startj]='R'
      l[starti+2][startj+1]='G'
    else:
      flag=True
      l[starti+2][startj+1]='R'
    l[starti+3][startj+1]='R'
    l[starti+3][startj+2]='B'
    if l[starti+3][startj+3]!='X' and
l[starti+3][startj+3]!='G' and flag:
      l[starti+3][startj+3]='B'
      l[starti+2][startj+2]='G'
    else:
      l[starti+2][startj+2]='B'
      if l[starti+3][startj+3]!='G':
l[starti+3][startj+3]='X'
    return

construct(n,0,0)
print_res(1)
    
