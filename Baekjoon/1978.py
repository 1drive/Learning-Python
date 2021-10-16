### 1978 소수 찾기
### https://www.acmicpc.net/problem/1978
import sys
N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
res = 0
for i in range(N):
    if M[i] in primes:
        res += 1
print(res)