from collections import defaultdict
n,m = map(int,input().split())
mydict = defaultdict(list)

for i in range(n):
    mydict[input()].append(i+1)

for j in range(m):
    print(*mydict[input()] or [-1])
