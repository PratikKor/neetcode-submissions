class Solution:
    def rob(self, nums: List[int]) -> int:
        e,o=0,0
        for n in nums:
            temp=max(n+e,o)
            e=o
            o=temp
        return o