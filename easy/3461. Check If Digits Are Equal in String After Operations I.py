class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        coef = [1]
        for i in range(1, n-1):
            coef.append(coef[-1] * (n-2-(i-1)) // i)
        a = 0
        b = 0
        for i in range(n-1):
            d1 = int(s[i])
            d2 = int(s[i+1])
            a = (a + coef[i] * d1) % 10
            b = (b + coef[i] * d2) % 10
        return a == b