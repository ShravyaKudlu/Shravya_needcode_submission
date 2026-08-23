class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        2, 2, 1, 3
        2, 1, 2, 4 [1 + 0 + 1 + 2 = 4]
        [1, 2, 3, 1, 2] , k = 3
        1, 3, 6, 7, 9, 1 + 2 + 3 = 6
        '''
        prefix = 0
        seen = {0: 1}
        count = 0
        for num in nums:
            prefix += num
            count += seen.get(prefix - k, 0)
            seen[prefix] = seen.get(prefix, 0) + 1 
        return count


        