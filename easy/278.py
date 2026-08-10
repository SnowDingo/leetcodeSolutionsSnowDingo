# implemented using binary search

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # left pointer
        left=0
        # right pointer
        right = n
        # while left is smaller or equal to right
        while left<=right:
            middle = (left+right)//2
            if(isBadVersion(middle) == True):
                right=middle-1
            else:
                # if too small then slide right
                left = middle +1
        return left