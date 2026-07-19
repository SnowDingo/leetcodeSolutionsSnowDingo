# This method utilizes the fact that we can consider the list's length to be fixed

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastnonzeroint = 0
        for i in range(0, len(nums)):
            if(nums[i] != 0):
                nums[lastnonzeroint]=nums[i]
                lastnonzeroint +=1
        while lastnonzeroint < len(nums):
            nums[lastnonzeroint] = 0
            lastnonzeroint+=1
        
        