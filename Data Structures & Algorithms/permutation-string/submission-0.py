class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        freq = Counter(s1)
        cur = {}
        size = len(s1)
        l = 0
        for r in range(len(s2)):
            cur[s2[r]] = 1 + cur.get(s2[r], 0)
            if r - l + 1 > size:
                cur[s2[l]] -= 1
                if cur[s2[l]] == 0:
                    del cur[s2[l]]
                l += 1
            if r - l + 1 == size and cur == freq:
                    return True
        return False