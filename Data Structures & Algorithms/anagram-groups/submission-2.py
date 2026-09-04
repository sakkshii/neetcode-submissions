class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}
        ls = []

        for i in range(len(strs)):
            ch = "".join(sorted(strs[i]))
            if ch not in hmap:
                hmap[ch] = [strs[i]]
            else:
                hmap[ch].append(strs[i])

        return list(hmap.values())