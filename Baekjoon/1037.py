### 1037 약수
### https://www.acmicpc.net/problem/1037
import sys
N = int(sys.stdin.readline())
Yaksu = []
Yaksu.extend(list(map(int, sys.stdin.readline().split())))
YangsuA = max(Yaksu) * min(Yaksu)
print(YangsuA)