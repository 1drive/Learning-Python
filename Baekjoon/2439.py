### 2439 별 찍기 - 2
### https://www.acmicpc.net/problem/2439
import sys
N = int(sys.stdin.readline().strip())
i = 1
while i <= N:
    print(" " * (N-i), "*" * i, sep="")
    i += 1