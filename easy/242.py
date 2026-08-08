# Slow solution but uses simple methods

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        sarr = list(s)
        tarr = list(t)
        sarr.sort()
        tarr.sort()
        if(sarr == tarr):
            return True
        else:
            return False
