class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = dict()
        
        for ele in nums:
            found[ele] = found.get(ele, 0) + 1
            if found[ele] == 2:
                return True
        return False
