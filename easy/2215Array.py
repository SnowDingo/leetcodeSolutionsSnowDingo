class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        whichbig = len(nums1) >= len(nums2)
        result = [[], []]
        for x in nums1:
            if(x not in nums2 and x not in result[0]):
                result[0].append(x)
        for y in nums2:
            if(y not in nums1 and y not in result[1]):
                result[1].append(y)
        return result
