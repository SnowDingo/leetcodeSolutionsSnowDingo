class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = []
        for i in range(0,len(nums)):
            for z in range(i,len(nums)):
                if(i!=z):
                    result.append((nums[i]-1)*(nums[z]-1))
        return max(result)