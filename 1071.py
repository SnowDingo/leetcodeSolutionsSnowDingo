class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # I first check if the two strings are equal to each other or not in order to make the algorithm quicker
        if(str1==str2):
            return str1
        result = [""]
        len1=len(str1)
        len2= len(str2)
        # next for each i we check how many times they have to be multiplied by and check if it is a divisor or not.
        for i in range(1,len2+1):
            times1 = len1//i
            times2= len2//i
            temp1 = ""
            temp2=""
            temp1 = times1*str2[0:i]
            temp2 = times2*str2[0:i]
            if (temp1==str1 and temp2==str2 ):
                result.append(str2[0:i])
        return max(result, key=len)