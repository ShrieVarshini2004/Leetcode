import heapq
class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        heap=[]
        for t in workerTimes:
            heapq.heappush(heap, (t, t, 2))
        result=0
        for _ in range(mountainHeight):
            accumulated, base, count = heapq.heappop(heap)
            result=max(result,accumulated)
            newcost=accumulated+base*count
            heapq.heappush(heap,(newcost,base,count+1))
        return result