### 1620 나는야 포켓몬 마스터 이다솜
### https://www.acmicpc.net/problem/1620
import sys
N, M = list(map(int, (sys.stdin.readline().split())))
dokam = {}
for i in range(N):
    dokam[sys.stdin.readline().strip()] = i+1
reverseDokam = {value:key for key, value in dokam.items()}
for j in range(M):
    Minput = sys.stdin.readline().strip()
    if Minput in dokam.keys():
        print(dokam.get(Minput))
    else:
        print(reverseDokam.get(int(Minput)))