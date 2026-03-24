class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isAlphanum(c):
            return(
                ord('0')<=ord(c)<=ord("9") or
                ord('A')<=ord(c)<=ord("Z") or
                ord('a')<=ord(c)<=ord("z")
            )
        left,right=0,len(s)-1
        while left<right:
            while left<right and not isAlphanum(s[left]):
                left+=1
            while left<right and not isAlphanum(s[right]):
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True