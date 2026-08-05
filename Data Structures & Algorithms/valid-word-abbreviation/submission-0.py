class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        m, n = len(word), len(abbr)
        while i < n and j < m:
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                num = 0
                while i < n and abbr[i].isdigit():
                    num = num*10 + int(abbr[i])
                    i += 1
                j += num
            else:
                if word[j] != abbr[i]:
                    return False
                i += 1
                j += 1
        return i == n and j == m






