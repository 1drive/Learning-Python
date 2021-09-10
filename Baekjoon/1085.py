### 1085 나머지
### https://www.acmicpc.net/problem/1085
import sys
x, y, w, h = list(map(int, sys.stdin.readline().split()))
toLeft, toRight, toTop, toBottom = x, w-x, h-y, y
print(min(toLeft, toRight, toTop, toBottom))