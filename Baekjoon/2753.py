### 2753 윤년
### https://www.acmicpc.net/problem/2753
import sys
Year = int(sys.stdin.readline())
isItYunYear = 0
if Year % 4 == 0:
    isItYunYear = 1
    if Year % 100 == 0:
        isItYunYear = 0
        if Year % 400 == 0:
            isItYunYear = 1
print(isItYunYear)
