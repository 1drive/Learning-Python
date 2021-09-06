### 1026 보물
### https://www.acmicpc.net/problem/1026
import sys
N = int(sys.stdin.readline())
A = []
A.extend(list(map(int, (sys.stdin.readline().split()))))
B = []
B.extend(list(map(int, (sys.stdin.readline().split()))))
acc = 0
for i in range(N):
    acc += max(A) * min(B)
    A.remove(max(A))
    B.remove(min(B))
print(acc)