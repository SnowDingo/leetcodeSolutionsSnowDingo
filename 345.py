class Solution:
    def reverseVowels(self, s: str) -> s:
        # First I check for edge case
        if(len(s)==1):
            return s
        # Then my algorithm is to first create a list that stores the indexes of the vowels and then swap each vowel using the list
        indexes = []
        for i in range(0,len(s)):
            # by using the lower() method I simplified the if statement
            if(s[i].lower() == "a" or s[i].lower() == "e" or s[i].lower() == "i" or s[i].lower() == "o" or s[i].lower() == "u" ):
                indexes.append(i)
        str1 = list(s)
        for i in range(0,len(indexes)//2):
            temp = str1[indexes[i]]
            temp2 = str1[indexes[-i-1]]
            str1[indexes[i]] = temp2
            str1[indexes[-i-1]] = temp
        return "".join(str1)