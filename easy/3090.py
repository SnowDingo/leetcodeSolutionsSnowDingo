class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxstr = ""
        temp =""
        for i in range(0,len(s)):
            occurences = dict({})
            for z in range(i,len(s)):
                if(s[z] in occurences.keys()):
                    if(occurences[s[z]]<=1):
                        occurences[s[z]] = occurences[s[z]]+1
                        temp = temp + s[z]
                    else:
                        break
                else:
                    occurences[s[z]] = 1
                    temp = temp + s[z]
            if len(temp)>len(maxstr):
                maxstr = temp
                temp = ""
            else:
                temp = ""
        return len(maxstr)