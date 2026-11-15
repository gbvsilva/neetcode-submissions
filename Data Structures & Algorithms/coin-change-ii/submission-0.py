from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def calc(i, amount):
            if amount == 0:
                return 1
            if i >= n or amount < 0:
                return 0

            pick = calc(i, amount - coins[i])
            skip = calc(i+1, amount)
            return pick + skip
        return calc(0, amount)