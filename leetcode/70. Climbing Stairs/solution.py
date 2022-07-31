class Solution:
    def climbStairs(self, n: int) -> int:
        
        if(n<2):
            return n;
        
        ans = [1,2];
        
        for i in range(2, n):
            ans.append(ans[i-1]+ans[i-2]);
            
        return ans[n-1];
