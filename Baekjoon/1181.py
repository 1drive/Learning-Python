### 1181 단어 정렬
### https://www.acmicpc.net/problem/1181
import sys
N = int(sys.stdin.readline())
listForWord = [sys.stdin.readline().strip() for _ in range(N)]
listForWord = list(set(listForWord))
listForWord.sort()
listForWord.sort(key = len)
print('\n'.join(listForWord))