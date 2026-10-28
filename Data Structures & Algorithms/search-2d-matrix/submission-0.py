from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [num for row in matrix for num in row]
        i = bisect_left(nums, target)
        return i < len(nums) and nums[i] == target
