class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = x
        rev = 0
        if x >= 2**31-1 or x <= -2**31: return 0
        if x < 0 :
            temp *= -1
        while temp != 0 :
            rev = rev * 10 + temp % 10
            temp = temp // 10
        if rev >= 2**31-1 or rev <= -2**31: return 0
        else :    
            if x < 0 :
                return rev * -1
            else :
                return rev * 1
