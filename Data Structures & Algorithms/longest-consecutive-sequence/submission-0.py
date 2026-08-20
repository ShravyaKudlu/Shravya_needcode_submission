class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums:
            num = n
            if num - 1 not in nums_set:
                cur = 1
                while num + 1 in nums_set:
                    cur += 1
                    num += 1
                longest = max(longest, cur)
        return longest





        