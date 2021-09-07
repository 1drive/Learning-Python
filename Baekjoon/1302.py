### 1302 베스트셀러
### https://www.acmicpc.net/problem/1302
import sys
N = int(sys.stdin.readline())
booksSold = {}
for i in range(N):
    bookSold = sys.stdin.readline().strip()
    if (bookSold in booksSold) == True:
        booksSold[bookSold] += 1
    else:
        booksSold[bookSold] = 1
gaJangManIPalIn = max(list(booksSold.values()))
sortedBooks = {key:value for key, value in booksSold.items() if value == gaJangManIPalIn}
sortedBooks = sorted(sortedBooks)
print(sortedBooks[0])