### 2480 주사위 세개
### https://www.acmicpc.net/problem/2480
import sys
A, B, C = list(map(int, sys.stdin.readline().split()))
Sangeum = 0 # 초기 상금은 0원일세
if A == B == C:
    Sangeum = 10000 + A * 1000
elif A == B or B == C or C == A:
    if A == B:
        Sangeum = 1000 + A * 100
    elif B == C:
        Sangeum = 1000 + B * 100
    else:
        Sangeum = 1000 + C * 100
else:
    Sangeum = max(A, B, C) * 100
print(Sangeum)