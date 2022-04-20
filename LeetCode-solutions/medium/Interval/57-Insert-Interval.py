class Solution:
  #use insert, makes it O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals,newInterval)
        ans = [intervals[0]]
        for s,e in intervals[1:]:
            if ans[-1][1]>=s:
                ans[-1][1] = max(ans[-1][1],e)  
            else:
                ans.append([s,e])
        return ans
