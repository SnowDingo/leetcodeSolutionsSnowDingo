class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # first i count the frequency using hashTable by first converting the list into a set
        arrprime = dict.fromkeys(set(arr),0)
        for i in range(0,len(arr)):
            arrprime[arr[i]] +=1
        values = list(arrprime.values())
        # then for each value i check if there is a duplicate or not
        for i in range(0,len(values)):
            for z in range(i,len(values)):
                if(values[i] == values[z] and i!=z):
                    return False
        return True
            