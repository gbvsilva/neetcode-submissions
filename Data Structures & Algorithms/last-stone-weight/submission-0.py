class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            stone = abs(x-y)
            if stone > 0:
                heapq.heappush(stones, -abs(x-y))
        return -stones[0] if stones else 0



