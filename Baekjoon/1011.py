### 1011 Fly me to the Alpha Centauri
### https://www.acmicpc.net/problem/1011
import math
import sys
T = int(sys.stdin.readline().strip())
def findMin(r):
    a, b = math.floor(math.sqrt(r)), math.ceil(math.sqrt(r))
    if r == a * a:
        b = a
    elif r <= b * b and r > a * b:
        a = b
    minab = (a + b - 1)
    return minab
thisisArray = []
for i in range(T):
    x, y = list(map(int, sys.stdin.readline().split()))
    range = y - x
    thisisArray.append(findMin(range))
for j in thisisArray:
    print(j)