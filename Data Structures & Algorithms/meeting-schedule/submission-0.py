"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        for i in range(1, len(intervals)):
            if end[i-1] > start[i]:
                return False
        return True
