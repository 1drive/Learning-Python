import sys
import math
D, H, W = list(map(int, sys.stdin.readline().split()))
n = D / math.sqrt((math.pow(H,2) + math.pow(W,2)))
print(math.floor(n * H))
print(math.floor(n * W))