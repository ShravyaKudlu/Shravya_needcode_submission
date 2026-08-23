class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(A: List[int], B: List[int]) -> List[int]:
            i, j, k = len(A) - 1, len(B) - 1, len(A) + len(B) - 1
            res = [0] * (k + 1)
            while i >= 0 and j >= 0:
                if A[i] >= B[j]:
                    res[k] = A[i]
                    i -= 1
                else:
                    res[k] = B[j]
                    j -= 1
                k -= 1
            while i >= 0:
                res[k] = A[i]
                i -= 1
                k -= 1
            while j >= 0:
                res[k] = B[j]
                j -= 1
                k -= 1
            return res
        if len(nums) == 1:
            return nums
        m = len(nums) // 2
        left = self.sortArray(nums[m:])
        right = self.sortArray(nums[:m])
        return merge(left, right)


            