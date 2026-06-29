class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        s = 0
        for i in range(len(patterns)):
            if patterns[i] in word:
                s += 1
        return s

        