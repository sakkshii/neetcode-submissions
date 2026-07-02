class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = 0 
        ed = len(s)-1

        while(st < ed):
            fchar = s[st]
            lchar = s[ed]

            if not fchar.isalnum():
                st+=1
                continue 
            if not lchar.isalnum():
                ed-=1
                continue

            if fchar.lower() == lchar.lower():
                st+=1
                ed-=1
            else:
                return False 
        return True 
        