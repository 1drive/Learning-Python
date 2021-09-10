### 2075 N번째 큰 수
### https://www.acmicpc.net/problem/2075
import heapq
import sys
N = int(input())
heap = []
for i in range(N):
    NsInput = list(map(int,sys.stdin.readline().split()))
    if not heap: 
        for tmp in NsInput:
            heapq.heappush(heap,tmp) ### 초기 Heap을 첫 줄 N개로 채움
    else:
        for tmp in NsInput:
            if heap[0] < tmp:
                heapq.heappush(heap,tmp) ### Heap이 N개의 input의 tmp보다 작으면 갈아끼움
                heapq.heappop(heap)
print(heap[0]) ### Heap 중 가장 작은 것 출력