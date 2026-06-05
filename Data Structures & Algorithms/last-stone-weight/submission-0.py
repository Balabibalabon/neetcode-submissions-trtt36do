import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)

        while heap and len(heap)>1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first == second:
                continue
            else:
                heapq.heappush(heap, -abs(first-second))
        
        if heap:
            return -heap[0]
        else:
            return 0