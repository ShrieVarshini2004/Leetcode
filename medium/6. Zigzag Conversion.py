class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        res=""
        cycle=2*(numRows-1)
        for r in range(numRows):
            for i in range(r,len(s),cycle):
                res+=s[i]
                if r>0 and r<numRows-1:
                    j=i+(cycle-2*r)
                    if j<len(s):
                        res+=s[j]
        return res