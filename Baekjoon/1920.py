### 1920 수 찾기
### https://www.acmicpc.net/problem/1920
import sys
N = int(sys.stdin.readline())
n = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())
m = sys.stdin.readline().split()

for l in m:
    sys.stdout.write('1\n') if l in n else sys.stdout.write('0\n')
