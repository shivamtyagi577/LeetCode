class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = x ** n
        if result >= 10**4 or result <= -10**4: return 0
        else :
            return result
