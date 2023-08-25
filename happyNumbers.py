import time
class Solution:
    def isHappy(self, n: int) -> bool:
        countFour = 0
        while(n!=1):
            curr = 0
            for x in str(n):
                curr += int(x)**2
            if(curr==n):return False
            n = curr 
            if(curr==4):countFour+=1
            if(countFour>2):return False         
        return True
    
a = Solution()
a.isHappy(12131)