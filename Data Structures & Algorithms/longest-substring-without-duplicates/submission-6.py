class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        visited = set()
        maxl = 0 
        fp = 0
        sp = fp
        while fp< len(s) and sp < len(s):
            if s[sp] not in visited:
                visited.add(s[sp])
                sp+=1
            else:
                if len(visited)>maxl:
                    maxl= len(visited)
                visited.remove(s[fp])
                fp+=1
        return max(maxl, len(visited))


           





