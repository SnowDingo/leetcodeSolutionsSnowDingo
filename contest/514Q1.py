class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices = sorted(prices,reverse=True)
        discounts = sorted(discounts,reverse=True)
        result = []
        remindex = 0
        if(len(discounts) <=len(prices)):
            for j in range(0,len(discounts)):
                result.append((prices[j]*(100-discounts[j]))/100)
                remindex = j
            for i in range(remindex+1,len(prices)):
                result.append(prices[i])
            return sum(result)
        else:
            for j in range(0,len(prices)):
                result.append((prices[j]*(100-discounts[j]))/100)
            return sum(result)