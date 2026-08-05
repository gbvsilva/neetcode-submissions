class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max_len = 0
        self.max_s = ''
        self.n = len(s)
        self.s = s

        for i in range(self.n):
            l = i
            r = i
            self.palin(l, r)
            l = i
            r = i + 1
            self.palin(l, r)
        return self.max_s

    def palin(self, l, r):
        while l >= 0 and r < self.n and self.s[l] == self.s[r]:
            if (r - l + 1) > self.max_len:
                self.max_len = r - l + 1
                self.max_s = self.s[l:r+1]
            l -= 1
            r += 1
