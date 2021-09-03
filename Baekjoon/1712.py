### 1712 손익분기점
### https://www.acmicpc.net/problem/1712
import sys
import math
A, B, C = list(map(int, sys.stdin.readline().split()))
if B >= C:
    print("-1")
else:
    print(math.floor(A/(C-B)) + 1)