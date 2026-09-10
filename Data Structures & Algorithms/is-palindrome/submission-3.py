class Solution:
    def isPalindrome(self, s: str) -> bool:
        fp = 0
        lp = len(s)-1

        while ( fp < lp):
            ch_fp = s[fp].lower()
            ch_lp = s[lp].lower()

            if ch_fp.isalnum() and ch_lp.isalnum():
                if ch_fp == ch_lp:
                    fp+=1
                    lp-=1
                else:
                    return False
            else:
                if not ch_fp.isalnum():
                    fp+=1
                else:
                    lp-=1
        return True

        