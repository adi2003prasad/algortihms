class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        dictData = {}
        counter = 0
        for x in pattern:
            if dictData.get(x, "")=="":
                dictData[x] = t[counter]
            else:
                return dictData[x]==t[counter]
            counter+=1