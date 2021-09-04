### 9498 시험 성적
### https://www.acmicpc.net/problem/9498
import sys
score = int(sys.stdin.readline())
if 90 <= score & score <= 100:
    print("A")
elif 80 <= score & score <= 89:
    print("B")
elif 70 <= score & score <= 79:
    print("C")
elif 60 <= score & score <= 69:
    print("D")
else:
    print("F")