# My algorithm was to convert the 2D array into 1D array then after the operation covert it back to 2D
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rowlen = len(grid)
        collen = len(grid[0])
        numitem = rowlen*collen
        temp = [0] * numitem
        grid2 = []
        for j in range(0,len(grid)):
            for i in range(0,len(grid[0])):
                slidenum = (k+j+(i+((collen-1)*j)))%len(temp)
                temp[slidenum]=grid[j][i]
        for i in range(0,len(temp),collen):
            grid2.append(temp[i:i+collen])
        return grid2