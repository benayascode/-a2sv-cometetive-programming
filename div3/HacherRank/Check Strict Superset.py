A = set(map(int,input().split()))
n = int(input())
for i in range(n):
    B = set(map(int,input().split()))
    if not B.issubset(A):
        print(False)
        break
else:
    print(True)
