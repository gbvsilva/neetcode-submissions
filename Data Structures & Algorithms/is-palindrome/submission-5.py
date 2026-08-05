class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s)-1
        while i < j:
            while i < j and not self.isalphanum(s[i]):
                i += 1
            while j > i and not self.isalphanum(s[j]):
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def isalphanum(self, c):
        return ((c >= 'a' and c <= 'z')
        or (c >= '0' and c <= '9'))