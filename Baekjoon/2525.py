### 2525 오븐 시계
### https://www.acmicpc.net/problem/2525
import sys
A, B = list(map(int, sys.stdin.readline().split()))
C = int(sys.stdin.readline())
B = B + C
Boverflow = B // 60
B = B - Boverflow * 60
A = A + Boverflow
if A >= 24:
    A %= 24
print(A, B)