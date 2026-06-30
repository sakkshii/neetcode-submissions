class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Map = {}
        if len(s) != len(t):
            return False
        
        for i in s:
            if i not in Map:
                Map[i]=1
            else:
                Map[i]+=1
        
        for i in t:
            if i in Map:
                Map[i]-=1
            else:
                return False
        result = all(v==0 for v in Map.values())
        return result