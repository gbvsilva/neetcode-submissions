class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        n = len(nums)
        for i in range(n):
            prod = nums[i]
            max_prod = max(max_prod, prod)
            for j in range(i+1,n):
                prod *= nums[j]
                max_prod = max(max_prod, prod)
        return max_prod