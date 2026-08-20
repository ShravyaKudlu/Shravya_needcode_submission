class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palandrome(sub_str: str) -> bool:
            return sub_str == sub_str[::-1]
        def backtrack(start: int, path: list[str]):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if palandrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
        res = []
        backtrack(0, [])
        return res
       
        