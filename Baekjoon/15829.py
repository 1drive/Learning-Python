### 15829 Hashing
### https://www.acmicpc.net/problem/15829
import sys
L = int(sys.stdin.readline())
nothashed = sys.stdin.readline().strip()
hashed = 0
for i in range(L):
    x = ord(nothashed[i])-96
    hashed += x * (31**(i))
print(hashed % 1234567891)