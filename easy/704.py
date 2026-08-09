class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left pointer
        left=0
        # right pointer
        right = len(nums)-1
        # while left is smaller or equal to right
        while left<=right:
            middle = (left+right)//2
            if(nums[middle] == target):
                return middle
            if(nums[middle] < target):
                # if too small then slide right
                left = middle +1
            else:
                # if too big then slide left
                right = middle -1
        return -1