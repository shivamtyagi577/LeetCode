class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        rev = 0
        if x >= 2**31-1 or x <= -2**31: return False
        if x < 0 :
            temp *= -1
        while temp != 0 :
            rev = rev * 10 + temp % 10
            temp = temp // 10
        if rev >= 2**31-1 or rev <= -2**31: return False
        else :    
            if x < 0   :
                return False
            elif rev == x :
                return True
