class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        arr.sort()
        target.sort()
        if(arr==target):
            return True
        
        return False