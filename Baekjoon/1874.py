### 1874 스택 수열
### https://www.acmicpc.net/problem/1874
import sys
from queue import Queue
n = int(sys.stdin.readline())
stack = []
ans = []
f = 0
c = 1
for i in range(n):
    num = int(sys.stdin.readline())
    while c <= num:
        stack.append(c)
        ans.append("+")
        c += 1
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        f = 1
        break
if f == 0:
    for i in ans:
        print(i)