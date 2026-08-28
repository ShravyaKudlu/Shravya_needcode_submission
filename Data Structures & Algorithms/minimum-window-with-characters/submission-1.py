class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        l = 0
        freqt = Counter(t)
        cur = {}
        need = len(freqt)
        have = 0
        best_r, best_l = float("inf"), 0
        for r in range(len(s)):
            cur[s[r]] = 1 + cur.get(s[r], 0)
            if s[r] in freqt and cur[s[r]] == freqt[s[r]]:
                have += 1
            while have == need:
                window = r - l + 1
                if window < best_r:
                    best_r = window
                    best_l = l
                cur[s[l]] -= 1
                if s[l] in freqt and cur[s[l]] < freqt[s[l]]:
                    have -= 1
                l += 1
        if best_r == float("inf"):
            return ""
        return s[best_l: best_l + best_r] 
                