class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hmap = {}

        for ch in t:
            if ch not in hmap:
                hmap[ch] = 1
            else:
                hmap[ch]+=1 

        for ch in s:
            if ch in hmap:
                hmap[ch]-=1
            else:
                return False

        return all(v==0 for v in hmap.values())

        