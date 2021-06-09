class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        sett = set(nums)
        if(len(sett) < 3):
            return max(sett)
        else :
            listt = list(sett)
            listt.sort()
            print(listt)
            return listt[-3]
