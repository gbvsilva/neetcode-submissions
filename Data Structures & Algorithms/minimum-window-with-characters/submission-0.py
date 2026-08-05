from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        countT = Counter(t)
        window = defaultdict(int)

        res, resLen = [-1, -1], float("inf")
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
                
        