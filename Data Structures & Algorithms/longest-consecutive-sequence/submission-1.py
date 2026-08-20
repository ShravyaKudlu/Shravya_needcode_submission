class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in nums_set:
                cur = 1
                while (n + cur) in nums_set:
                    cur += 1
                longest = max(longest, cur)
        return longest





        