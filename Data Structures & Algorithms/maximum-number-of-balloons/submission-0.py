class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        
        # 'l' and 'o' need to be divided by 2
        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )

        