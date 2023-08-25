class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicts, dictt = {}, {}
        counter = 0
        for x, y in zip(s, t):
            dicts[x] = dicts.get(x, []).append(counter)
            dictt[y] = dictt.get(y, []).append(counter)
            counter+=1
        l = dicts.values()
        for x in dictt.values():
            if x not in l:return False
        return True