class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = longest = most_freq = 0
        counter = defaultdict(int)
        for r in range(len(s)):
            counter[s[r]] += 1
            most_freq = max(most_freq, counter[s[r]])
            while (r - l + 1) - most_freq > k:
                counter[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest