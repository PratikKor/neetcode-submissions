class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0
        for i in range(len(nums)):
            if nums[i]==0: 
                res=max(res,cnt) 
                cnt=0
            elif nums[i]==1:
                cnt+=1
        return max(cnt,res)