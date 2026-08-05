class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        quadruplets = []
        for a in range(n-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, n-2):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c = b + 1
                d = n - 1
                x = target - (nums[a]+nums[b])
                while c < d:
                    sum_ = nums[c] + nums[d]
                    if sum_ < x:
                        c += 1
                    elif sum_ > x:
                        d -= 1
                    else:
                        quadruplets.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
        return quadruplets
