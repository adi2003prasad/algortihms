class Solution:
    def add(self, currCombination, limits, index):
        if(currCombination[-1]==limits[-1]):
            if(currCombination[index]==limits[index]):
                return self.add(currCombination, limits, index-1)
            else:
                for x in range(-1, index, -1):
                    currCombination[x]=1
                
                currCombination[index]+=1
            return currCombination
        
        currCombination[-1]+=1
        return currCombination
    
    def letterCombinations(self, digits: str) :
        data = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        limits = []
        k = len(digits)
        if(k==1):
            ans = []
            for x in data[digits]:
                ans.append(x)
            return ans
        for x in digits:
            limits.append(len(data[x]))
            
        def printCombo(combo):
            # print(combo)
            ans = ""
            for x in range(len(combo)):
                ans+=data[digits[x]][combo[x]-1]
            return ans
        currComb = [1]*len(digits)
        alls = []
        while(currComb!=limits):
            alls.append(printCombo(currComb))
            currComb = self.add(currComb, limits, -2)
        alls.append(printCombo(currComb))
        return alls
a = Solution()
print(len(a.letterCombinations("239")))