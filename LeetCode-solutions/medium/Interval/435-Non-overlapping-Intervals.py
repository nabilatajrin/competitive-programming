class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x: x[1])
        n, count = len(intervals), 1
        if n == 0: return 0
        curr = intervals[0]
        
        for i in range(n):
            if curr[1] <= intervals[i][0]:
                count += 1
                curr = intervals[i]
        return n - count   
    
    
    #2nd solution
    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
