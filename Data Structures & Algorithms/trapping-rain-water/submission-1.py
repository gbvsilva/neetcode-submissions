class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [0]*n, [0]*n
        maxHeight = 0
        for i in range(n):
            maxLeft[i] = maxHeight
            maxHeight = max(maxHeight, height[i])
        maxHeight = 0
        for i in range(n-1, -1, -1):
            maxRight[i] = maxHeight
            maxHeight = max(maxHeight, height[i])
        count = 0
        for i in range(n):
            amount = min(maxLeft[i], maxRight[i]) - height[i]
            count += amount if amount > 0 else 0
        return count