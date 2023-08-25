class Solution:
    def isValid(self, s: str) -> bool:
        score = {"()":0, "[]":0, "{ }":0}
        for x in str:
            if(x=="("):
                score[0] = score.get(0, 0)+1
            elif(x==")"):
                score[0] = score.get(0, 0)-1
            elif(x=="["):
                score[1] = score.get(1, 0)+1
            elif(x=="]"):
                score[1] = score.get(1, 0)-1
            elif(x=="{"):
                score[2] = score.get(2, 0)+1
            elif(x=="}"):
                score[2] = score.get(2, 0)-1
            else:
                continue
        for x in score:
            if(score[x]!=0):
                return False
        return True
                