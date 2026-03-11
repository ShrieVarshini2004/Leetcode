class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        result=0
        position=0
        while n>0:
            bit=n&1
            if bit==0:
                result+=(1<<position)
            n=n>>1
            position+=1
        return result