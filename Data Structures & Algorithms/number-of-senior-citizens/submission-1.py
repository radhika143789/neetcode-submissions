import re
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            s = re.split(r'([a-zA-Z])', i)
            if int(s[2][0:2]) > 60:
                count +=1
        return count
                