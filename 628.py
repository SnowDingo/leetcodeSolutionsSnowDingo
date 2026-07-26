
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # I use the fact that - * - = +
        # So +++ or --+ compare
        nums = sorted(nums, reverse=True)
        one = two = three = -1000000000
        negativeone = negativetwo = 10000000
        for i in range(0,len(nums)):
            print(nums[i])
            print((one,two,three,negativeone,negativetwo))
            if nums[i] >= one:
                three = two
                two = one
                one = nums[i]
            elif nums[i] >= two:
                three = two
                two = nums[i]
            elif nums[i] >= three:
                three = nums[i]
            if nums[i] <= negativeone:
                negativetwo = negativeone
                negativeone = nums[i]
            elif nums[i] <= negativetwo:
                negativetwo = nums[i]
        if(one*two*three>=negativeone*negativetwo*one):
            return one*two*three
        else:
            return negativeone*negativetwo*one

