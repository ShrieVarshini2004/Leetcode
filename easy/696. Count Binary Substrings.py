class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups=[]
        last=None
        count=0
        for ch in s:
            if ch==last:
                count+=1
            else:
                if count>0:
                    groups.append(count)
                last=ch
                count=1
        groups.append(count)
        result=0
        for i in range(1,len(groups)):
            result+=min(groups[i],groups[i-1])
        return result