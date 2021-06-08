class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        listt = []
        count_zero = nums.count(0)
        #print(count_zero)
        for i in range(count_zero):
            listt.append(0)
            nums.remove(0)
        nums.extend(listt)
