### 2231 분해합
### https://www.acmicpc.net/problem/2231
import sys
N = int(sys.stdin.readline())
stringN = str(N)
startLine = N - (len(stringN) * 9)
if startLine < 0:
    startLine = 1
result = 0
while startLine <= N:
    listedStartLine = list(map(int, str(startLine)))
    if startLine + sum(listedStartLine) == N:
        result = startLine
        break
    else:
        startLine += 1
print(result)

### 29200 KB, 72 ms