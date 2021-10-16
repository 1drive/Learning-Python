### 2108 통계학
### https://www.acmicpc.net/problem/2108
import sys
from statistics import multimode
N = int(sys.stdin.readline())
hereNumbersCome = []
for i in range(N):
    temp = int(sys.stdin.readline())
    hereNumbersCome.append(temp)
SansulAVG = round(sum(hereNumbersCome) / N)
ChungangValue = sorted(hereNumbersCome)
ChungangValue = ChungangValue[(N+1)//2-1]

multimodeNumbers = multimode(sorted(hereNumbersCome))
ChoibinValue = multimodeNumbers[1] if len(multimodeNumbers) > 1 else multimodeNumbers[0]

qaqa = max(hereNumbersCome) - min(hereNumbersCome)
print(SansulAVG)
print(ChungangValue)
print(ChoibinValue)
print(qaqa)