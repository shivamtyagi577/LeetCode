class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        odd_list = []
        even_list = []
        listt = list(nums)
        del nums[N : ]
        #print(nums)
        for i in range(N):
            if((listt[i] % 2) == 0):
                even_list.append(listt[i])
            else :
                odd_list.append(listt[i])
        even_list.extend(odd_list)
        return even_list
