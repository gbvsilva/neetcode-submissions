class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        s_set = set()
        longest = 0
        while r < len(s):
            if s[r] not in s_set:
                s_set.add(s[r])
                r += 1
            else:
                s_set.remove(s[l])
                longest = max(longest, r-l)
                print(r,l)
                l += 1
        return max(longest, r-l)
