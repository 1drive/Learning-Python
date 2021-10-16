### 2798 블랙잭
### https://www.acmicpc.net/problem/2798
import sys
N, M = list(map(int, sys.stdin.readline().split()))
cards = list(map(int, sys.stdin.readline().split()))
cards = sorted(cards, reverse=True)
tempSum = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = cards[i] + cards[j] + cards[k]
            if temp <= M:
                tempSum.append(temp)
print(max(tempSum))