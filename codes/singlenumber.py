class Solution:
    '''The question gives us a list where every number has a single duplicate expect 
    for a single number and we have to find that number'''
    
    # by this code i reduced the memory required buy 
    # needed a whole lot of runtime
    # 1000 ms
    def singleNumber(self, nums: List[int]) -> int:
        while(len(nums)>=1):
            t = nums[0]
            nums.pop(0)
            if(t in nums):nums.pop(nums.index(t))
            else:return t
            
    # now to have a faster code
    
    # 130 ms 90% fast
    def singleNumber(self, nums: List[int]) -> int:
        t = {}
        for x in nums:
            t[x] = t.get(x, 0)+1
        for x, y in zip(t.keys(), t.values()):
            if(y==1):return x
            else:continue 
        
        
