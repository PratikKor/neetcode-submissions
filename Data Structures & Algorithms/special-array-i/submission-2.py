class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        st=nums[0]%2
        for i in nums:
            if(i%2!=st):
                return False
            st=(st+1)%2
        return True