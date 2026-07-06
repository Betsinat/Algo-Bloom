class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : (x[0] , -x[1]))
        i = 0
        while i < len(intervals) - 1:
            if intervals[i + 1][1] <= intervals[i][1]:
                del intervals[i + 1] 
            else:
                i += 1  
        return len(intervals)