# This problem is about merging two strings together in alternating order

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1len = len(word1)
        word2len = len(word2)
        result = ""
        # I used maxi variable to keep track of how many times loop occured
        maxi = 0
        # My code simply divides the situation into three categories
        # Two cases where one string is longer than other and the simplest case where both strings have an equal length
        if(word1len>word2len):
            for i in range(0,word2len):
                result = result + word1[i] + word2[i]
                maxi=i
            result = result + word1[maxi+1:word1len] 
        elif (word1len < word2len):
            for i in range(0,word1len):
                maxi=i
                result = result + word1[i] + word2[i]
            result = result + word2[maxi+1:word2len]
        else:
            for i in range(0,word2len):
                result = result + word1[i] + word2[i]
        return result
