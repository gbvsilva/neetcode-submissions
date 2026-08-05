import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(nums)
        count = 1
        max_count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                count += 1
            elif nums[i] - nums[i-1] > 1:
                max_count = max(max_count, count)
                count = 1
        return max(max_count, count)

        