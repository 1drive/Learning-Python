### 2920 음계
### https://www.acmicpc.net/problem/2920
import sys
N = list(map(int, sys.stdin.readline().split()))
if N == sorted(N, reverse=False):
    print("ascending")
elif N == sorted(N, reverse=True):
    print("descending")
else:
    print("mixed")