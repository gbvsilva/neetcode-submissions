class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = max_len = 0
        freq = defaultdict(int)
        for r, ch in enumerate(s):
            freq[ch] += 1
            while len(freq) > 2:
                ch = s[l]
                freq[ch] -= 1
                if freq[ch] == 0:
                    del freq[ch]
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len