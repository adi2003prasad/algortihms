class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        j = []
        j.append("0"*k)
        goOn = True
        if(j[0] in s):
            pass
        else:
            goOn = False
        l = int("0", 2)
        
        for _ in range(1, 2**k):
            if goOn==True:
                l+=int("1", 2)
                z = bin(l)[2:]
                if(len(z)!=k):
                    g = k-len(z)
                    z = ("0"*g)+z

                if(z in s):
                    pass
                else:
                    goOn = False
            else:
                return False
        return goOn
    def hasallOtherway(self, s: str, k: int) -> bool:
        hashmap = []
        lenOfHashmap = 0
        ourNum = 2**k+3
        for x in range(len(s)):
            t = s[x:x+k]
            # print(t)
            if(t not in hashmap):
                hashmap.append(t)
                lenOfHashmap+=1

            if(lenOfHashmap==ourNum):
                hashmap.sort()
                print("1111111" in hashmap)
                return True
            else:
                pass
        return lenOfHashmap==ourNum
            
            
            
a = Solution()
print(a.hasallOtherway("011101100101110101101000011111101011111101110100111100010000010110010010011100110001110010101101011010010001101111000111110000001010100101111001111010110001111011001110100010001111000111010001111100101011100001001011101100010101010110001011110101001101001001111101000100011101110100100100101101110000000110001011100100111111001000100100010011001000101101100010010010001111010111010011110111110001010100000110000111010110001100100110111000111010111000010100100100101011001111010110010101110101000011011101000110001001100111100011000100110010101100001111000100101001111001100001010100100100110100101100111000110010110101010110010110001111010110101111011011100111001010101001011000101101110100001110011110001011000011100011111001110011111101110001110010000111010011110001011010100101110010110110100011111011110010100011111000000001011100110000010101110110111", 7))