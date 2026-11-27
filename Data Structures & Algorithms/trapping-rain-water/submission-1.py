class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        lm=[0] * n #array for max in left side
        rm=[0] * n #arr for max in right side
        lm[0]=height[0] 
        rm[n-1]=height[n-1]
        for i in range(1,n): #loop to get max in left of each ele
            lm[i]=max(lm[i-1],height[i])
        for i in range(n-2,-1,-1): #loop to get max in right of each ele
            rm[i]=max(rm[i+1],height[i])
        
        res=0
        for i in range(n):
            res+=min(lm[i],rm[i])-height[i] #formula to get water trapped
        return res
            