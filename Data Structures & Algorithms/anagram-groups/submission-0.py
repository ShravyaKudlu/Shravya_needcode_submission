class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            hashmap["".join(sorted(s))].append(s)
        return [value for value in hashmap.values()]