### 2884 알람 시계
### https://www.acmicpc.net/problem/2884
import sys
H, M = list(map(int, sys.stdin.readline().split()))
time = H * 60 + M
if time < 45:
    time += 1440
time -= 45
H, M = time // 60, time % 60
print(H, M)