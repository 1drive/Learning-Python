### 1427 단어 정렬
### https://www.acmicpc.net/problem/1427
import sys
N = int(sys.stdin.readline())
sortednumber = 0
b = list(str(N))
b.sort()
for i in range(len(b)):
    sortednumber += int(b[i]) * 10 ** i
print(sortednumber)