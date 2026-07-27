class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        length = min([len(s) for s in strs])
        prefix = strs[-1]

        for s in strs:
            for i in range(length):
                if prefix[i] != s[i]:
                    length = i
                    break
        
        return strs[-1][:length]
