class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        last = nums[0]
        for x in nums[1:]:
            if x!=last+1:return False
        return True
            
    def newidea(self, nums):
        # used the simple idea that the sum of numbers of a sequence of n integers is n(n+1)/2
        # hence any number not in this sum will eventually be our number
        a = sum(nums)
        k = len(nums)
        return (k*(k+1)/2) - a