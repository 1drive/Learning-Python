# 1094 막대기
# https://www.acmicpc.net/problem/1094
import sys
X = str(bin(int(sys.stdin.readline())))
X = X[2:]
sol = 0
for i in X:
    if i == "1":
        sol += 1
print(sol)
