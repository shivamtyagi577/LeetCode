class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3 = []
        num3.extend(nums1)
        for i in range(len(nums2)):
            num3.insert(i,nums2[i])
        num3.sort()
        N = len(num3)
        print(N)
        if((N%2)!=0):
            print(N,N,N)
            median = N//2
            #median+=1
            print(median)
            rt=round(num3[median],5)
            return rt
        else:
            print(N,N)
            median1 = N//2
            median2 = median1 - 1
            rt = ((num3[median1] + num3[median2])/2)
            if(((num3[median1]) % 2 != 0) or ((num3[median2]) % 2) != 0 ) :
                rt = rt + 0.5
            if(((num3[median1]) % 2 != 0) and ((num3[median2]) % 2) != 0 ) :
                rt = rt - 0.5
            print(num3[median1], num3[median2])
            print(rt)
            rt = round(rt,5)
            return float(rt)
        
