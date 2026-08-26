class Solution:
    def maxDifference(self, s: str) -> int:
        scount = {}

        for a in s:
            if a in scount:
                scount[a] += 1
            else:
                scount[a] = 1

        best_odd = float('-inf')
        best_even = float('inf')

        for a in scount:
            if scount[a] % 2 == 1:
                best_odd = max(best_odd, scount[a])
            else:
                best_even = min(best_even, scount[a])

        return best_odd - best_even