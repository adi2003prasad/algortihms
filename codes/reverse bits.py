class Solution:
    def reverseBits(self, n: int) -> int:
        copp = int(n)
        remaining = None
        t = ""
        while remaining!=0:
            t += str(copp%2)
            remaining = copp//2
            copp = remaining
        while(len(t)<32):
            t += "0"
        return int(t, 2)
        
        
a = Solution()
print(a.reverseBits(43261596))