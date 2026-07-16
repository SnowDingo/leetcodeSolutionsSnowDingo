# Very dirty code but still AC. What I did is I followed a flowchart of edge cases with if statements
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(n==0):
            return True
        if(len(flowerbed) == 1):
            if(flowerbed[0] == 0):
                return n<=1
            else:
                return False
        if(n==len(flowerbed)):
            return False
        index = []
        if(flowerbed[0] == 0 and flowerbed[1] == 0):
            index.append(0)
        if (flowerbed[-1] == 0 and flowerbed[-2] == 0 and len(flowerbed) -1 not in index):
            index.append(len(flowerbed)-1)
        for i in range(1,len(flowerbed)-1):
            if(flowerbed[i] == 1):
                continue
            if(flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and (i-1 not in index) and (i+1 not in index) ):
                index.append(i)
        if(n<=len(index)):
            return True
        else:
            return False