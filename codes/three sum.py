class Solution:
    def threeSum(self, nums):
        '''
        this is a brute force approach where i am taking all possible combinations and 
        chekcing the condition of the question'''
        l = len(nums)
        ans = []
        if l>3:
            for x in range(l):
                a = nums[x]
                for y in range(x+1, l):
                    b = nums[y]
                    c = -(a+b)
                    if c in nums[y+1: l]:
                        newlist = [a, b, c]
                        newlist.sort()
                        if newlist not in ans:
                            ans.append(newlist)
            return ans
        if l==3:
            if sum(nums)==0:return [nums]
            return []
    
    def threeSum2(self, nums):
        '''the way i am thinking will be faster'''
        nums.sort()
        l = len(nums)
        ans = []
        '''we will find the median point '''
        if l>3:
            for a in range(l//2):
                for c in range(l-1, a+2, -1):
                    b = a+(c-a)//2
                    # print(a, b, c, "indexes")
                    while a!=b!=c:
                        x = nums[a]
                        y = nums[b]
                        z = nums[c]
                        su = x+y+z
                        # print(x, y, z, "real values")
                        if su==0:
                            t = [x, y, z]
                            t.sort()
                            if t in ans:
                                break
                            else:
                                ans.append(t)
                            break
                        elif su<0:
                            b+=1
                        else:
                            b-=1
            return ans
        if l==3:
            if sum(nums)==0:
                return [nums]
            else:return ans


                

a = Solution()
print(a.threeSum2([-1,0,1,2,-1,-4]))
        