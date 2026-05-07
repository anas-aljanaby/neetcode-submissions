class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        if not len(nums):
            return res
        i, k = 0, 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return True
        return False
