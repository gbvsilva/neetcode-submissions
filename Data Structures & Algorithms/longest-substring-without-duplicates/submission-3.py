class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = l = 0
        charSet = set()
        for r, ch in enumerate(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                #maxLen = max(maxLen, r-l+1)
                l += 1
            charSet.add(ch)
            maxLen = max(maxLen, r-l+1)
        return maxLen
        