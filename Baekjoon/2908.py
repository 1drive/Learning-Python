### 2908 상수
### https://www.acmicpc.net/problem/2908
import sys
A, B = list(map(int, sys.stdin.readline().split()))
print(max(int(str(A)[::-1]), int(str(B)[::-1])))