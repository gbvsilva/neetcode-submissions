class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_s = ''
        n = len(s)

        def palin(l, r):
            nonlocal max_len, max_s
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    max_s = s[l:r+1]
                l -= 1
                r += 1

        for i in range(n):
            palin(i, i)
            palin(i, i+1)
        return max_s
