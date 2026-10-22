class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif={}
        for i,n in enumerate(nums):
            dife=target-n
            if dife in dif:
                return [dif[dife],i]
            dif[n]=i