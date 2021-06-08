class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        expected = list(heights)
        expected.sort()
        for i in range(len(heights)):
            if( expected[i] == heights[i]):
                continue
            else :
                count+=1
        return count
