### 2292 벌집
### https://www.acmicpc.net/problem/2292
import sys
N = int(sys.stdin.readline())
a, b = 0, 1
ans, tryCount = 0, 1
while ans == 0:
    if a <= N and N <= b:
        ans = tryCount
    else:
        a = b + 1
        b = b + 6 * tryCount
        tryCount += 1
print(tryCount)