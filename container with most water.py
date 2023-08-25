class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxVol = 0
        leftpointer = 0
        rightpointer = len(height)-1
        while leftpointer!=rightpointer:
            if height[leftpointer]<height[rightpointer]:
                curheight = height[leftpointer]
                curvol = curheight*(rightpointer-leftpointer)
                leftpointer+=1
            else:
                curheight = height[rightpointer]
                curvol = curheight*(rightpointer-leftpointer)
                rightpointer-=1
            if curvol>maxVol:maxVol = curvol
        return maxVol