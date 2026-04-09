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

        result = count = 0
        start_pointer, end_pointer = 0, 0

        while start_pointer < len(intervals):
            if start[start_pointer] < end[end_pointer]:
                start_pointer += 1
                count += 1
            else:
                end_pointer += 1
                count -= 1
            result = max(result, count)
        return result