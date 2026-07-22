class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        fp = 0 
        maxlen = 0 

        for sp in range(len(s)):

            if s[sp] not in hmap:
                hmap[s[sp]]=1
            else:
                hmap[s[sp]]+=1
            
            winsize = sp-fp+1
            maxFreq = max(hmap.values())

            if winsize - maxFreq > k :
                hmap[s[fp]]-=1
                fp+=1 
            maxlen = max(sp-fp+1, maxlen)

        return maxlen

        
