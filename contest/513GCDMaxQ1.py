import math
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        result = 0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(i==j):
                    continue
                else:
                    result = max(result, ((int(nums[i])*int(nums[j]))//math.gcd(int(nums[i]),int(nums[j]))**2))
        return result