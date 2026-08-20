class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)
        print(words)
        output = []        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    output.append(words[i])
        return list(set(output))
