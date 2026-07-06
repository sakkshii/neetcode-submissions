class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp = 0 
        ep = len(s)-1 

        while(sp<ep):
            sChar = s[sp]
            eChar = s[ep]

            if sChar.isalnum():
                sChar = sChar.lower()
            else:
                sp+=1
                continue

            if eChar.isalnum():
                eChar = eChar.lower()
            else:
                ep-=1
                continue 
            
            if sChar == eChar:
                sp+=1
                ep-=1
            else:
                return False
        return True

