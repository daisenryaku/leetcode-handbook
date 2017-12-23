class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        size = len(timeSeries)
        ans = duration * size;
        for i in range(1, len(timeSeries)):
            ans -= max(0, duration-(timeSeries[i]-timeSeries[i-1]))
        return ans
