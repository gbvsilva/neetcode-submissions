class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for val in nums[k:]:
            if val > heap[0]:
                heapq.heapreplace(heap, val)
        return heap[0]
