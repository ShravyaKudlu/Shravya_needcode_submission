class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = nums[0]
        count = 1
        for i in range(1, len(nums)):
            count += 1 if nums[i] == cand else -1
            if count == 0:
                cand = nums[i]
                count = 1
        return cand