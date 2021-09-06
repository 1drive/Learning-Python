### 1065 한수
### https://www.acmicpc.net/problem/1065
import sys
import math
N = int(sys.stdin.readline())
Hansu = 0
for i in range(N):
    A = i+1
    tmp = []
    for l in str(A):
        tmp.append(l)
    if len(tmp)==1:
        Hansu += 1
    elif len(tmp)==2:
        Hansu += 1
    elif len(tmp)==3:
        if int(tmp[0]) - int(tmp[1]) == int(tmp[1]) - int(tmp[2]):
            Hansu += 1
print(Hansu)