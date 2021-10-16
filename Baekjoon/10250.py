### 10250 ACM 호텔
### https://www.acmicpc.net/problem/10250
import sys
import math
T = int(sys.stdin.readline().strip())
for i in range(T):
    H, W, N = list(map(int, sys.stdin.readline().split()))
    YY, XX = N-H*(math.ceil(N / H)-1), math.ceil(N / H)
    if len(str(XX)) == 1:
        XX = "0" + str(XX)
    print(YY,XX,sep="")