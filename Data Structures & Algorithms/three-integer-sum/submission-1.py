class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and nums[i - 1] == v:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = nums[l] + nums[r] + v
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else: 
                    res.append([nums[l], v, nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
        
             
        