from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @cache
        def count(i, j):
            if i >= m:
                return n - j
            if j >= n:
                return m - i
            if word1[i] == word2[j]:
                return count(i+1, j+1)
            opt1 = count(i+1, j)
            opt2 = count(i, j+1)
            opt3 = count(i+1, j+1)
            return 1 + min(opt1, opt2, opt3)
        return count(0, 0)
