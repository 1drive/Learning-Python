### 11047 동전 0
### https://www.acmicpc.net/problem/11047
import sys
N, K = list(map(int, sys.stdin.readline().split()))
coins = []
for i in range(N):
    tmp = int(sys.stdin.readline().strip())
    coins.append(tmp)
coinLeft = K
count = 0
for i in range(N):
    coinUsed = coinLeft // coins[-i-1]
    if coinUsed > 0:
        coinLeft -= coins[-i-1] * coinUsed
        count += coinUsed
print(count)