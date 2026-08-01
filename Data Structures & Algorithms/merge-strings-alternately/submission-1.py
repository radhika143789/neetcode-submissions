class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        one_pointer,two_pointer = 0, 0

        while one_pointer < len(word1) and two_pointer < len(word2):
            result += word1[one_pointer] + word2[two_pointer]
            one_pointer += 1
            two_pointer += 1

        if len(word1) > len(word2):
            result += word1[one_pointer:]
        else:
            result += word2[two_pointer:]

        return result