### 1003 피보나치 함수
### https://www.acmicpc.net/problem/1003
import sys
T = int(sys.stdin.readline().strip())
fibonacci = [[1, 0], [0, 1]]
i = 2
while i < 43:
    fibonacci.append([fibonacci[i-2][0] + fibonacci[i-1][0], fibonacci[i-2][1] + fibonacci[i-1][1]])
    i += 1
for j in range(T):
    whatDoYouWant = int(sys.stdin.readline().strip())
    print(fibonacci[whatDoYouWant][0], fibonacci[whatDoYouWant][1])