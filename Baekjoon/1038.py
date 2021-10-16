### 1038 감소하는 수
### https://www.acmicpc.net/problem/1038
import sys
import math
N = int(sys.stdin.readline())
found = 0
testNum = 1
while found < N:
    if testNum < 10:
        testNum += 1
        found += 1
    elif testNum > 9:
        listForTest = list(str(testNum))
        print(testNum, sorted(listForTest, reverse=True) == listForTest, list(set(listForTest)) == sorted(listForTest, reverse=True), sorted(list(set(listForTest)), reverse=True),sorted(listForTest, reverse=True) ,found)
        if sorted(list(set(listForTest)), reverse=True) == sorted(listForTest, reverse=True) and sorted(listForTest, reverse=True) == listForTest:
            testNum += 1
            found += 1
        else:
            testNum += 1
    else:
        testNum += 1
print(testNum - 1, found)
