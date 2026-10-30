class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Phase 1: Append intervals before newInterval.
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Phase 2: Merge overlapping intervals.
        while i < n and intervals[i][0] <= newInterval[1]:
            # TODO: Update newInterval's start and end.
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # TODO: Append the merged newInterval.
        result.append(newInterval)

        # Phase 3: Append remaining intervals.
        # TODO
        result.extend(intervals[i:])

        return result