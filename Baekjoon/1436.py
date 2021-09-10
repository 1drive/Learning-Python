### 1436 영화감독 숌
### https://www.acmicpc.net/problem/1436
import sys
N = int(sys.stdin.readline())
i, target = 666, 0
while target < N:
    if '666' in str(i):
        target += 1
    i += 1
print(i-1)