
# This solution uses array's index to store the max then remove that max to find the second max and multiply. 
# this method does not involve sorting
class Solution:
    def maxProduct(self, n: int) -> int:
        numbers = []
        for i in range(0, len(str(n))):
            numbers.append(int(str(n)[i]))
        max1=max(numbers)
        del numbers[numbers.index(max1)]
        return max(numbers)*max1
