### 1120 문자열
### https://www.acmicpc.net/problem/1120
import sys
from tempfile import tempdir
A, B = map(list, sys.stdin.readline().split())
N = len(B)
diff = 0
tmplist = []
tempDiff = 0
if len(A) < N:
    for b in range(N - len(A) + 1):
        forCompareB = B[b:b+len(A)]
        for i in range(len(A)):
            if A[i] != forCompareB[i]:
                tempDiff += 1
        tmplist.append(tempDiff)
        tempDiff = 0
        diff = min(tmplist)
elif len(A) == N:
    for i in range(N):
        if A[i] != B[i]:
            diff += 1
print(diff)