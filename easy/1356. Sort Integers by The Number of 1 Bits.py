class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def countbits(x):
            count=0
            while x:
                x=x&(x-1)
                count+=1
                x=x//2
            return count
        arr.sort()
        arr.sort(key=lambda x:countbits(x))
        return arr
