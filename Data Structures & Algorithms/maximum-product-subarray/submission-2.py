class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1
        for n in nums:
            tmp = currMax * n
            currMax = max(tmp, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            res = max(res, currMax, currMin)
        return res