### 2751 수 정렬하기 2
### https://www.acmicpc.net/problem/2751
import sys
N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for i in range(N):
    print(nums[i])