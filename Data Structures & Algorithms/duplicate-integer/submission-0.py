class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s1={}
        for ind,val in enumerate(nums):
            if val not in s1:
                s1[val]=ind
            elif val in s1:
                return True
        return False