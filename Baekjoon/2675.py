### 2675 문자열 반복
### https://www.acmicpc.net/problem/2675
import sys
T = int(sys.stdin.readline())
for i in range(T):
    tmpString = ''
    R, S = sys.stdin.readline().split()
    S = list(S)
    for j in range(len(S)):
        tmpString = tmpString + (S[j] * int(R))
    print(tmpString)