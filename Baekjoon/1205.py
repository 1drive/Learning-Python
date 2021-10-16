### 1205 등수 구하기
### https://www.acmicpc.net/problem/1205
import sys
N, NewScore, P = list(map(int, sys.stdin.readline().split()))
ArrayScores = list(map(int, sys.stdin.readline().split()))
if len(ArrayScores) == P:
    if min(ArrayScores) >= NewScore:
        print(-1)
    else:
        ArrayScores.append(NewScore)
        ArrayScores = sorted(ArrayScores, reverse=True)
        if (ArrayScores.index(NewScore)+1) <= P:
            print(ArrayScores.index(NewScore)+1)
        else:
            print(-1)
else:
    ArrayScores.append(NewScore)
    ArrayScores = sorted(ArrayScores, reverse=True)
    if (ArrayScores.index(NewScore)+1) <= P:
            print(ArrayScores.index(NewScore)+1)
    else:
        print(-1)