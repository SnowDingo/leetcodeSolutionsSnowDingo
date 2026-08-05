
class Solution:
    def reverseWords(self, s: str) -> str:
        s= " " + s
        if(" " not in s):
            return s
        words = []
        counter = 0
        newstr = ""
        # this loop registers words into the words array
        for i in range(1,len(s)):
            if(s[i] == " "):
                if(counter != i and s[i-1] == " "):
                    counter = i
                elif(counter!=i and s[i-1] != " "):
                    words.append((counter,i+1))
                    counter = i
            else:
                if(i==len(s)-1):
                    words.append((counter,i+1))
        print(words)
        # Now the swap part
        for i in range(0,len(words)//2):
            temp = words[i]
            temp2 = words[-i-1]
            words[i] = temp2
            words[-i-1] = temp
        # Now make a new string
        for i in range(0,len(words)):
            if(i!=len(words)-1):
                newstr = newstr + s[words[i][0]:words[i][1]].replace(" ", "") + " "
            else:
                newstr = newstr + s[words[i][0]:words[i][1]].replace(" ", "")
        return newstr