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
            if s[i].isdigit():
                num += s[i]
                i += 1
                continue
            if s[i] == '#':
                j = len(num)
                length = int(num)
                start = i + 1
                ans.append(s[start:start+length])
                # print('num:', num, 'i:', i, 'j:', j, 'start:', start, 'len:', length, 'ans:', ans)
                num = ''
            i = start + length
        return ans
