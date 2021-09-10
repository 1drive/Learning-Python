### 2562 최댓값
### https://www.acmicpc.net/problem/2562
import sys
A = []
tmp = 0
for i in range(9):
    tmp = int(sys.stdin.readline())
    A.append(tmp)
print(max(A))
print(A.index(max(A))+1)