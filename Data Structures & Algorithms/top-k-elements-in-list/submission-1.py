class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = sorted(c.keys(), key=lambda num: c[num], reverse=True)
        return c[:k]