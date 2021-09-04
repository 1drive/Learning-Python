### 5543 상근날드
### https://www.acmicpc.net/problem/5543
import sys
price = [0, 0, 0, 0, 0]
for i in range(5):
    price[i] = int(sys.stdin.readline())
setPrice = min(price[0], price[1], price[2]) + min(price[3], price[4]) - 50
print(setPrice)