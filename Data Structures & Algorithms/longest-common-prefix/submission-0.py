class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minPrefix = min(strs, key = len)
        prefix = ""
        for i, c in enumerate(minPrefix):
            if all (c == s[i] for s in strs):
                prefix += c 
            else:
                break 
        return prefix