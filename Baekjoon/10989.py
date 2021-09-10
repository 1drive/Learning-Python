### 10989 수 정렬하기 3
### https://www.acmicpc.net/problem/10989
import sys
N = int(sys.stdin.readline())
A = [0] * 10000
for i in range(N):
    A[int(sys.stdin.readline())-1] += 1 
for i in range(10000):
    if A[i] != 0:
        for j in range(A[i]):
            print(i+1)