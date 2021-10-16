### 2609 최대공약수와 최소공배수
### https://www.acmicpc.net/problem/2609
from curses import nl
import sys
import math
N, M = list(map(int, sys.stdin.readline().split()))
gcdNM = math.gcd(N, M)
print(gcdNM)
print(N*M//gcdNM)