class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        maxLeft, maxRight = height[l], height[r]
        count = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                count += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                count += maxRight - height[r]
        return count