### 2588 곱셈
### https://www.acmicpc.net/problem/2588
import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
lastDigit, middleDigit, firstDigit = str(B)[2], str(B)[1], str(B)[0]
print(A * int(lastDigit))
print(A * int(middleDigit))
print(A * int(firstDigit))
print(A * B)