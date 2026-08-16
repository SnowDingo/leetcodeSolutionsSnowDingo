class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) ==1):
            return nums
        counter = {0:0,1:0,2:0}
        for i in range(0,len(nums)):
            match nums[i]:
                case 0:
                    counter[0] = counter[0]+1
                case 1:
                    counter[1] = counter[1]+1
                case 2:
                    counter[2] = counter[2]+1
        current = 0
        count = 0
        for x in range(0,3):
            for z in range(0, counter[x]):
                nums[count] = x
                count +=1
            

            