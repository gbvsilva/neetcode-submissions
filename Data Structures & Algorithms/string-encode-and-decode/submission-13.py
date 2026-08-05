class Solution:

    def encode(self, strs: List[str]) -> str:
        str = ''.join([f'{len(s)}#{s}' for s in strs])
        print(str)
        return str

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        num = ''
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j
        return ans
