
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        c = a/b
        result = 0
        for i in range(0, len(nums)):
            counter = {"odd":0, "even":0}
            for j in range(i,len(nums)):
                if(nums[j] %2==0):
                    counter["even"] = counter["even"]+1
                else:
                    counter["odd"] = counter["odd"] +1
                if(counter["odd"] > 0 and counter["even"]/counter["odd"] <= c):
                    result +=1
        return result