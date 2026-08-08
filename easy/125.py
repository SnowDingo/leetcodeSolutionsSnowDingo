class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first for each character I check if it is alphanumeric letter by using isalnum and lower all characters
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        print(s)
        # Semi Binary search method where I minimize the iteration by half
        for i in range(0,len(s)//2):
            if(s[i] != s[-(i+1)]):
                return False
        return True