# This is a solution of problem 283 without the use of a pointer. This beats 80% of the submission in terms of the memory space

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point0 = 0
        for i in range(0,len(nums)):
            if(nums[point0]==0):
                nums.append(0)
                del nums[point0]
            else:
                point0+=1
