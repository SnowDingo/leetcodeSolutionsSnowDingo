class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) == 1):
            return 0
        # pointer solution. keep a pointer that points to the minum and update if necessary to traverse the list only once. Learned the code from Geeks for Geeks
        currentmin = prices[0]
        result = 0
        for i in range(1,len(prices)):
            currentmin = min(currentmin,prices[i])
            result = max(result, prices[i]-currentmin)
        return result