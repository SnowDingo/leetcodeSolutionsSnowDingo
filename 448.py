# A solution that utilizes the property of hashSet

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num = set(nums)
        result = []
        for i in range(1,len(nums)+1):
            if(i not in num):
                result.append(i)
        return result