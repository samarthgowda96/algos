import heapq

heap=[]

heapq.heappush(heap,30)
heapq.heappush(heap,2)
heapq.heappush(heap,10)
heapq.heappush(heap,1)
heapq.heappush(heap,22)
minimun= heapq.heappop(heap)
minn= heapq.heappop(heap)

print(heap)
print(minimun)
print(minn)
