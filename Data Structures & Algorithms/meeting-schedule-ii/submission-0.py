"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        rooms = 0
        j = 0
        for i in range(len(intervals)):
            if start[i] < end[j]:
                rooms += 1
            else:
                j+=1

        return rooms

        