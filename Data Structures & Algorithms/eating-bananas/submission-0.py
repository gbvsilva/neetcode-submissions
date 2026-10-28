class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            k = (left + right) // 2
            total_hours = sum(math.ceil(pile / k) for pile in piles)
            if total_hours > h:
                left = k + 1
            else:
                right = k - 1
        return left