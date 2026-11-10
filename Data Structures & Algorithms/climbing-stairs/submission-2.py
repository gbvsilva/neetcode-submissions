class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1
        for _ in range(1, n):
            tmp = one + two
            one = two
            two = tmp
        return two