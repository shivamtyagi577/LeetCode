class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        listt = []
        #if(len(arr)==1):
            #listt.insert(len(arr)-1,-1)
        for i in range(1,len(arr)):
            listt.insert(i-1,max(arr[i:]))
            #print(listt,arr[i-1])
        listt.insert(len(arr)-1,-1)
        return listt
        
