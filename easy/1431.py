class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in range(0,len(candies)):
            # I simply check if the new cookie count is larger than the maximum item in the list
            if candies[i]+extraCandies >=max(candies):
                result.append(True)
            else:
                result.append(False)
        return result
