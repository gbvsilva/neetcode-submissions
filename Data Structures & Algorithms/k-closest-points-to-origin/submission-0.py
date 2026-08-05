class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def key(point: list):
            return (math.sqrt(point[0]**2 + point[1]**2), point)
        heap = [key(point) for point in points]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            if heap:
                res.append(heap[0][1])
                heapq.heappop(heap)
        return res
