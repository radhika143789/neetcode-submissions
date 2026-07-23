"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Step 1: Sort intervals by their start times
        intervals.sort(key=lambda x: x.start)
        
        # Step 2: Check each meeting against the previous one
        for i in range(1, len(intervals)):
            prev_meeting = intervals[i - 1]
            curr_meeting = intervals[i]
            
            # If current meeting starts before the previous one ends
            if curr_meeting.start < prev_meeting.end:
                return False
                
        return True
