class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        print(arr[-1])
        if(len(arr) < 3):
            return False
        elif(max(arr) == arr[0] or max(arr) == arr[-1]):
            return False
        for i in range(1,len(arr)):
            if(arr[i-1] < arr[i]):
                count+=1
            else :
                break
        print(count,i)
        for i in range(i,len(arr)):
            if(arr[i-1] > arr[i]):
                count+=1
            else:
                break
        print(count)
        if(count == (len(arr)-1)):
            return True
        else:
            return False
