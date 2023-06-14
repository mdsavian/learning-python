import heapq

minHeap = []

heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 99)
heapq.heappush(minHeap, 1)

print(minHeap)

while len(minHeap):
    print(heapq.heappop(minHeap))

# to create a max heap we need to multiply by -1
maxHeap = []
heapq.heappush(maxHeap, -1 * 16)
heapq.heappush(maxHeap, -1 * 199)
heapq.heappush(maxHeap, -1 * 11)
heapq.heappush(maxHeap, -1 * -111)


while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# build from array
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)

while len(arr):
    print(heapq.heappop(arr))
