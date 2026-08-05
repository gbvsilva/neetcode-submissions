class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = max_len = 0
        freq = defaultdict(int)
        for r, ch in enumerate(s):
            freq[ch] += 1
            while len(freq) > 2:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len