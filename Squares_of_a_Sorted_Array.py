class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        listt = []
        for i in range(len(nums)):
            listt.append(nums[i]**2)
            #print(listt)
        listt.sort()
        return listt
        
