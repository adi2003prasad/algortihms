class Solution:
    def longestPalindrome(self, s: str) -> str:
        def slower(start, end):
            while(start>-1) and (end<len(s)):
                if s[start]!=s[end]:break
                start-=1
                end+=1
            return s[start+1:end]
        ans = ""
        for x in range(len(s)):
            t = slower(x, x) # assuming the center is the element itself
            if(len(t)>len(ans)):ans = t
            tt = slower(x, x+1) # assuming the center is between the numbers
            if(len(tt)>len(ans)):ans = tt
            
        return ans
