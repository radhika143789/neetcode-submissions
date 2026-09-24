from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = len(s)
        t_counts = defaultdict(int)
        for c in t:
            t_counts[c] += 1
        
        window_counts = defaultdict(int)
        for c in s:
            window_counts[c] += 1
        
        #First we check we have enough letters if we take the whole string
        for c in t_counts.keys():
            if t_counts[c] > window_counts[c]:
                return ""

        #Now we know we have enough, we first find the [0,right] shortest legitimate
        critical_letter = None
        left = 0
        for right in range(l-1,-1,-1):
            c = s[right]
            if window_counts[c] == t_counts[c]:
                break
            else:
                window_counts[c] -=1
        #Now [0,right] holds the shortest legitimate
        while window_counts[s[left]] > t_counts[s[left]]:
            window_counts[s[left]] -=1
            left +=1 
        best_length = right - left + 1
        best_left, best_right = left, right
        while right < l-1:
            right +=1
            right_letter = s[right]
            window_counts[right_letter] += 1
            while window_counts[s[left]] > t_counts[s[left]]:
                window_counts[s[left]] -=1
                left +=1 
            #We have a valid window
            window_length = right - left+1
            if window_length < best_length:
                best_left, best_right = left, right
                best_length = window_length 


        return s[best_left:best_right+1]
