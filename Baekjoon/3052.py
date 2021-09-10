### 3052 나머지
### https://www.acmicpc.net/problem/3052
import sys
A = []
for _ in range(10):
    A.append(int(sys.stdin.readline()) % 42)
print(len(list(set(A))))