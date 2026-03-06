class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        segments=0
        for i in range(len(s)):
            if s[i]=='1' and (i==0 or s[i-1]=='0'):
                segments+=1
            if segments>1:
                return False
        return True