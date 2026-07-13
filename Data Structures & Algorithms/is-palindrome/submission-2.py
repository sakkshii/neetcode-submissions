class Solution:
    def isPalindrome(self, s: str) -> bool:
        fp =0 
        ep = len(s)-1 

        while(fp<ep):
            if s[fp].isalnum() and s[ep].isalnum():
                if s[fp].lower() == s[ep].lower():
                    fp+=1
                    ep-=1
                else:
                    return False
            else:
                if not s[fp].isalnum():
                    fp+=1
                else:
                    ep-=1
            
        return True 
        