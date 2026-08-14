class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        i = 0
        result = []
        while (len(str(i)) <= n):
            ist = str(i)
            sum = 0
            for z in range(0,len(ist)):
                sum += int(ist[z])
            if(sum == s):
                result.append(i)
            i +=1
        if(len(result) == 0):
            return -1
        else:
            return max(result)