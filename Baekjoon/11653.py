### 11653 소인수분해
### https://www.acmicpc.net/problem/1978
import sys
N = int(sys.stdin.readline())
i = 2
while N > 1:
    if N % i == 0:
        N = N / i
        print(i)
    else:
        i += 1
if N > 1:
    print(N)